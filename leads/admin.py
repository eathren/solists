from django.contrib import admin
from .models import Lead
# Register your models here.
class LeadAdmin(admin.ModelAdmin):
    list_display = ("title", "author")

admin.site.register(Lead, LeadAdmin)