from django import forms
from base_app.models import Picture


class UploadForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['post_picture', 'description']