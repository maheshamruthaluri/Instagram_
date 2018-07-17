from base_app.models import User
from django import forms


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', 'password')

