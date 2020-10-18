from django.urls import path

from .views import SignupPageView, DeveloperListView, ProfilePageView

urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup'),
    path('developers/', DeveloperListView.as_view(), name="developers" ),
    path('profile/' , ProfilePageView.as_view(), name='profile')
]
