from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.db.models import Q
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LeadCreationForm

# Create your views here.
from .models import Lead


class LeadListView(ListView):
    queryset = Lead.objects.filter(status=1).order_by('-created_at')
    model = Lead
    context_object_name = "lead_list"
    template_name = 'home.html'
    paginate_by = 10
    ordering=['-created_at']


class LeadDetailView(DetailView):
    model = Lead
    context_object_name = "lead"
    template_name = 'leads/lead_detail.html'


class SearchResultsView(ListView):  
    model = Lead
    context_object_name = 'lead_list'
    template_name = 'leads/search_results.html'
    # queryset = Lead.objects.filter(title__icontains="react")
    def get_queryset(self):  
        query = self.request.GET.get('q')
        return Lead.objects.filter(
            Q(title__icontains=query) | Q(job_type__icontains=query) | Q(company__icontains=query) | Q(country__icontains=query) | Q(skills__icontains=query) | Q(country=query)
        )


class PostLeadView(LoginRequiredMixin, CreateView):
    form_class = LeadCreationForm
    model = Lead
    success_url = reverse_lazy('orders')
    template_name = 'leads/create_lead.html'

    def form_valid(self, form):
        form.instance.user_author = self.request.user
        return super().form_valid(form)

# class UpdateLeadView(UpdateView):
#     model = Lead
#     template_name='leads/update_lead.html'
#     fields = ['title', 'description', 'body']
