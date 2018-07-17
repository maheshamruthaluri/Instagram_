from django import forms
from django.contrib.auth.models import User


class userForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',  'placeholder': 'name'}),
                               required=True, max_length=100)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
                            required=True, max_length=100)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
                                 required=True, max_length=100)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
                                required=True, max_length=100)
    # bio = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Tell about yourself'}), required=True, max_length=1000)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
                               required=True, max_length=50)
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}), required=True,
        max_length=50)

    # profile_picture = forms.ImageField()

    class Meta():
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']