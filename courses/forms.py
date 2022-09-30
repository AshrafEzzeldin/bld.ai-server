from django import forms
from models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInputss)

    class Meta:
        model = User
