from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User



class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = "__all__"


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name']
