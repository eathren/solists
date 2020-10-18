from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import CustomUser

from .forms import CustomUserCreationForm


# Create your views here.
class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class DeveloperListView(ListView):
    model = CustomUser
    context_object_name = "developer_list"
    template_name = "developers/developer_list.html"