from django.urls import path

from .views import LeadListView, LeadDetailView, SearchResultsView, PostLeadView

urlpatterns = [
    path('', LeadListView.as_view(), name="home"),
    path('leads/<uuid:pk>', LeadDetailView.as_view(), name="lead_detail"),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('leads/create-lead', PostLeadView.as_view(), name="post_lead")

]