from django.contrib import admin
from .models import Lead
# Register your models here.
class LeadAdmin(admin.ModelAdmin):
    list_display = ("title", "author",'id', "user_author", "company", "created_at", "updated_at",)

admin.site.register(Lead, LeadAdmin)