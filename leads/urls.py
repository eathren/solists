from django.contrib import admin
from django.urls import path, include

from .views import HomePageView

urlpatterns = [
     path('admin/', admin.site.urls),
     # path('', HomePageView.as_view(), name='home'),

     # User management
     path('accounts/', include('allauth.urls')),

     # Local apps
     path('', include('leads.urls'))
]
