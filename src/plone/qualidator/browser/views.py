from Products.Five.browser import BrowserView
from plone.qualidator.validators.validator import validate_core


class QualidationView(BrowserView):

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.categories = {
            'core': dict(results=[], validator=validate_core),
        }

    def render(self):
        return self.index()

    def __call__(self):
        self.handle_validation()
        return self.render()

    def title(self):
        return u'Content quality overview for: {}'.format(self.context.title)

    def handle_validation(self):
        for key in self.categories:
            self.categories[key]['results'] = \
                self.categories[key]['validator'](self.context)
