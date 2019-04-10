from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic import RedirectView, TemplateView


class DocumentationView(TemplateView):
    template_name = 'documentation.html'


class FaviconView(RedirectView):
    url = staticfiles_storage.url('img/favicons/favicon.ico')
    permanent = False


class HomeView(TemplateView):
    template_name = 'home.html'


class RobotsView(TemplateView):
    template_name = 'robots.txt'
    content_type = 'text/plain'
