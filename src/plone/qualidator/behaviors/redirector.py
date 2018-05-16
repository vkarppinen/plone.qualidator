from plone.autoform.interfaces import IFormFieldProvider
from zope.interface.declarations import provider
from plone.supermodel import model
import transaction


@provider(IFormFieldProvider)
class IQualidatable(model.Schema):
    pass


def do_redirect(trans, obj=None):
    request = getattr(obj, 'REQUEST', None)
    if request:
        url = obj.absolute_url() + '/@@content_qa'
        request.response.redirect(url)


def handle_redirect(object, event):
    """
    Subbscriber handler for qualidator behavior.
    Redirects to content quality view.
    """
    kwargs = dict(
        obj=object,
    )
    transaction.get().addAfterCommitHook(do_redirect, kws=kwargs)
