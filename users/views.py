from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView

from .models import CustomUser

from .forms import CustomUserCreationForm, CustomUserChangeForm


# Create your views here.
class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class DeveloperListView(ListView):
    model = CustomUser
    context_object_name = "developer_list"
    template_name = "developers/developer_list.html"
   

class ProfilePageView(generic.UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('profile')
    template_name = 'account/profile.html'

    def get_object(self):
        return self.request.user

class ProfileDetailView(DetailView):
    model = CustomUser
    context_object_name = "user"
    template_name = 'developers/profile.html'