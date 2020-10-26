from django.urls import path
from .views import HomePageView, TermsOfServicePageView, PrivacyPolicyPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('terms-of-service/', TermsOfServicePageView.as_view(), name='terms_of_service'),
    path('privacy-policy/', PrivacyPolicyPageView.as_view(), name='privacy_policy')
]