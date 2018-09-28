from django import forms
from .models import Tourer
from django.forms import CharField, Form, PasswordInput
class Tourer_form(forms.ModelForm):
    class Meta:
        model = Tourer
        widgets = {
        'password': forms.PasswordInput(),
    }