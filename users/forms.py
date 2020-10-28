from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django_countries.fields import CountryField
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.http import HttpResponseRedirect
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'username' )

class CustomUserChangeForm(UserChangeForm):
    # hides password field that userchangeform includes by default
    password = None

    class Meta(UserChangeForm):
        model = CustomUser
        fields = ( 'email', 'first_name', 'last_name',  'published', 'description', 'country', 'developer', 'designer', 'job_title', 'experience', 'linkedin', 'github', 'website', 'stackoverflow', 'contact_email', 'allow_contact', 'skills',)
