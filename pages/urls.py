from django.urls import path
from .views import HomePageView, SupportPageView, TermsOfServicePageView, PrivacyPolicyPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('terms-of-service/', TermsOfServicePageView.as_view(), name='terms_of_service'),
    path('privacy-policy/', PrivacyPolicyPageView.as_view(), name='privacy_policy'),
    path('support/', SupportPageView.as_view(), name='support')
]