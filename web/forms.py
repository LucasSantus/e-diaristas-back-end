from django import forms
from .models import Diarista

class DiaristaForm(forms.ModelForm):

    class Meta:
        model = Diarista
        exclude = ('__all__')