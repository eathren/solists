from django.views.generic import ListView, DetailView
from django.db.models import Q

# Create your views here.
from .models import Lead

class LeadListView(ListView):
    model = Lead
    context_object_name = "lead_list"
    template_name = 'home.html'

class LeadDetailView(DetailView):
    model = Lead
    context_object_name = "lead"
    template_name = 'lead_detail.html'

class SearchResultsView(ListView): # new
    model = Lead
    context_object_name = 'lead_list'
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        return Lead.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
