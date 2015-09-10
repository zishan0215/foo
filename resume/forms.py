from django import forms
from .models import FilebabyFile

class FilebabyForm(forms.ModelForm):
    """Upload files with this form"""
    class Meta:
        model = FilebabyFile
        fields = ('f',)