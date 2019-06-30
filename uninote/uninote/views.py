from django.views.generic import TemplateView

class Homepage(TemplateView):
    template_name = 'homepage.html'


class Test(TemplateView):
    template_name = 'test.html'

class Thanks(TemplateView):
    template_name = 'thanks.html'

class About(TemplateView):
    template_name = 'about.html'

class Discussions(TemplateView):
    template_name = 'discussions.html'

class Response(TemplateView):
    template_name = 'response.html'
