from django.contrib import admin
from .models import Lead
# Register your models here.
class LeadAdmin(admin.ModelAdmin):
    list_display = ("title", "author",'id', 'status', "user_author", "country", "company", "created_at", "updated_at",)
    list_filter = ("status",)

admin.site.register(Lead, LeadAdmin)