from django.contrib import admin
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import*


class CustomUserAdmin(BaseUserAdmin):
    add_form = UserChangeForm
    form = UserCreationForm
    model = CustomUser
    list_display = ["pkid","id","email" , "first_name","last_name","date_joined"] 
    search_fields = ["email", "first_name", "last_name"]
   
    fieldsets = (
        ('User Details', {'fields': ('email','password')}),
        ('Personal Details', {'fields': ('first_name', 'last_name')}),
        ('Permission Info', {
            'classes': ('wide',),
            'fields': ('is_staff', 'is_active', 'is_superuser','groups', 'user_permissions', 'date_joined',)}
        )
    )
    
    add_fieldsets = (
        ('Personal Info', {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name','password1', 'password2')}
        ),
    )
    ordering = ('email',)
    filter_horizontal = ['groups', 'user_permissions']


admin.site.unregister(Group)
admin.site.register(CustomUser, CustomUserAdmin)
