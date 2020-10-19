from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms

from .models import Lead

class LeadCreationForm(forms.ModelForm):
    class Meta():
        model = Lead
        fields = ('company','user_author')