from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms
from django.contrib.auth import get_user_model

from .models import Lead


class LeadCreationForm(forms.ModelForm):
    class Meta():
        model = Lead
        fields = ('title',  'logo', 'company',  'description', 'job_type', 'experience',
                  'developer', 'designer', 'country',   'skills', 'contact_info', 'application_link')
        exclude = ["user_author"]
        
