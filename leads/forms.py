from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms
from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Lead


class LeadCreationForm(forms.ModelForm):
    class Meta():
        model = Lead
        fields = ('title',  'logo', 'company',  'description', 'job_type', 'experience',
                  'developer', 'designer', 'country',   'skills', 'contact_info', 'application_link')
        exclude = ["user_author"]
       
        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.helper = FormHelper()
        #     self.helper.layout = Layout(
        #         Row(
        #             Column('title', css_class='form-group col-md-6 mb-0'),
        #             Column('company', css_class='form-group col-md-6 mb-0'),
        #             css_class='form-row'
        #         ),
        #         'address_1',
        #         'address_2',
        #         Row(
        #             Column('city', css_class='form-group col-md-6 mb-0'),
        #             Column('state', css_class='form-group col-md-4 mb-0'),
        #             Column('zip_code', css_class='form-group col-md-2 mb-0'),
        #             css_class='form-row'
        #         ),
        #         'check_me_out',
        #         Submit('submit', 'Sign in')
        # )