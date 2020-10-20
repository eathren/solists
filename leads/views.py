from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.db.models import Q
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LeadCreationForm

# Create your views here.
from .models import Lead


class LeadListView(ListView):
    model = Lead
    context_object_name = "lead_list"
    template_name = 'home.html'


class LeadDetailView(DetailView):
    model = Lead
    context_object_name = "lead"
    template_name = 'leads/lead_detail.html'


class SearchResultsView(ListView):  # new
    model = Lead
    context_object_name = 'lead_list'
    template_name = 'search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        return Lead.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )


class PostLeadView(LoginRequiredMixin, CreateView):
    form_class = LeadCreationForm
    model = Lead
    success_url = reverse_lazy('home')
    template_name = 'leads/create_lead.html'

# class UpdateLeadView(UpdateView):
#     model = Lead
#     template_name='leads/update_lead.html'
#     fields = ['title', 'description', 'body']
