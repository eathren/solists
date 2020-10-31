from django.views.generic import TemplateView
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class TermsOfServicePageView(TemplateView):
    template_name="terms_of_service.html"

class PrivacyPolicyPageView(TemplateView):
    template_name="privacy_policy.html"

class SupportPageView(TemplateView):
    template_name="support.html"