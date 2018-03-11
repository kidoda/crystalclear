from django.views import generic

class AboutPageView(generic.TemplateView):
    template_name = 'pages/about.html'
