from django import forms
from .models import TemporaryUpload


class TemporaryUploadForm(forms.ModelForm):
    class Meta:
        model = TemporaryUpload