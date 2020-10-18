from django.urls import path

from .views import SignupPageView, DeveloperListView

urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup'),
    path('developers/', DeveloperListView.as_view(), name="developers" )
]
