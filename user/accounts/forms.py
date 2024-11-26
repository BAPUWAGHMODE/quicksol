from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'date_of_birth', 'password1', 'password2', 'profile_picture']

class LoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']
