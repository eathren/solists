from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm

from .models import CustomUser

# CustomUser = get_user_model()



class CustomUserAdmin(UserAdmin):
    fieldsets = (
       (None, {'fields': ('email', 'password', )}),
    ('Personal info', {'fields': ('first_name', 'last_name', 'published', 'developer', 'designer','description', 'experience', 'country', 'job_type', 'skills')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    limited_fieldsets = (
        (None, {'fields': ('email', )}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'twitter', 'photo')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    change_password_form = auth_admin.AdminPasswordChangeForm
    model = CustomUser
    list_display = ['email', 'username','id',  "country", "experience", 'developer']
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('email',)
    readonly_fields = ('last_login', 'date_joined',)

admin.site.register(CustomUser, CustomUserAdmin)