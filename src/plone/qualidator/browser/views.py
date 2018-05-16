from Products.Five.browser import BrowserView
from plone.qualidator.validators.validator import validate_dublin_core


class QualidationView(BrowserView):

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.categories = [
            dict(name='Dublin core',
                 results=[],
                 validator=validate_dublin_core),
        ]

    def render(self):
        return self.index()

    def __call__(self):
        self.handle_validation()
        return self.render()

    def title(self):
        return u'Content quality overview for: {}'.format(self.context.title)

    def handle_validation(self):
        for cat in self.categories:
            cat['results'] = cat['validator'](self.context)

    def categories(self):
        return self.categories
