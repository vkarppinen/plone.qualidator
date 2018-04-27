# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.qualidator.testing import PLONE_QUALIDATOR_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that plone.qualidator is properly installed."""

    layer = PLONE_QUALIDATOR_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plone.qualidator is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'plone.qualidator'))

    def test_browserlayer(self):
        """Test that IPloneQualidatorLayer is registered."""
        from plone.qualidator.interfaces import (
            IPloneQualidatorLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IPloneQualidatorLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONE_QUALIDATOR_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['plone.qualidator'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if plone.qualidator is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'plone.qualidator'))

    def test_browserlayer_removed(self):
        """Test that IPloneQualidatorLayer is removed."""
        from plone.qualidator.interfaces import \
            IPloneQualidatorLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IPloneQualidatorLayer,
            utils.registered_layers())
