from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView

from .models import CustomUser

from .forms import CustomUserCreationForm, CustomUserChangeForm


# Create your views here.
class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'



class ProfilePageView(LoginRequiredMixin, generic.UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('profile')
    template_name = 'account/profile.html'
    context_object_name = "dev"

    def get_object(self):
        return self.request.user

class DeveloperListView(ListView):
    model = CustomUser
    queryset = CustomUser.objects.filter(published=1, developer=1).order_by('-date_joined')
    context_object_name = "dev_list"
    template_name = "developers/developer_list.html"
    paginate_by = 40
      

class DeveloperDetailView(DetailView):
    model = CustomUser
    context_object_name = "dev"
    template_name = 'developers/profile.html'

class DesignerListView(ListView):
    model=CustomUser
    queryset = CustomUser.objects.filter(published=1, designer=1).order_by('-date_joined')
    context_object_name = "dev_list"
    template_name = "designers/designer_list.html"
    paginate_by = 40

class DesignerDetailView(DetailView):
    model = CustomUser
    context_object_name = "designer"
    template_name = 'designers/profile.html'