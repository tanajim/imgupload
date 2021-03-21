from django import forms
from .models import Imguploading

class Imgforms(forms.ModelForm):
    class Meta:
        model = Imguploading
        fields = ['uname','profile']