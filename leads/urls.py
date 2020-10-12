from django.urls import path

from .views import LeadListView, LeadDetailView, SearchResultsView

urlpatterns = [
    path('', LeadListView.as_view(), name="lead_list"),
    path('<uuid:pk>', LeadDetailView.as_view(), name="lead_detail"),
    path('search/', SearchResultsView.as_view(), name='search_results')

]