from plone.autoform.interfaces import IFormFieldProvider
from zope.interface.declarations import alsoProvides
from plone.supermodel import directives
from plone.supermodel import model
from zope import schema


class IQualidatable(model.Schema):
    directives.fieldset(
        'social',
        label=u'Social',
        fields=('lanyrd',),
    )

    lanyrd = schema.URI(
        title=u"Lanyrd link",
        description=u"Add URL",
        required=False,
    )


alsoProvides(IQualidatable, IFormFieldProvider)
