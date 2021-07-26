from django.contrib import admin
from .models import User
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin
# from django_rest_passwordreset.models import ResetPasswordToken

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm

    fieldsets =(
        *UserAdmin.fieldsets,
        (
            'User details',
            {
                'fields':(
                'gender',
                'birthday'
            )
            
            }
        )
    )

admin.site.register(User,CustomUserAdmin)
