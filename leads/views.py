from django.views.generic import ListView, DetailView
# Create your views here.
from .models import Lead

class LeadListView(ListView):
    model = Lead
    context_object_name = "lead_list"
    template_name = 'leads/lead_list.html'

class LeadDetailView(DetailView):
    model = Lead
    template_name = 'leads/lead_detail.html'