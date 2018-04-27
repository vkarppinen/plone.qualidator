# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import plone.qualidator


class PloneQualidatorLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=plone.qualidator)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plone.qualidator:default')


PLONE_QUALIDATOR_FIXTURE = PloneQualidatorLayer()


PLONE_QUALIDATOR_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONE_QUALIDATOR_FIXTURE,),
    name='PloneQualidatorLayer:IntegrationTesting',
)


PLONE_QUALIDATOR_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONE_QUALIDATOR_FIXTURE,),
    name='PloneQualidatorLayer:FunctionalTesting',
)


PLONE_QUALIDATOR_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONE_QUALIDATOR_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='PloneQualidatorLayer:AcceptanceTesting',
)
