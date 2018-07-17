from base_app.models import User
from django import forms


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('name', 'gender', 'age', 'bio', 'profile_picture')

