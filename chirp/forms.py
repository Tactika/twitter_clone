from django import forms

from .models import Chirp

class NewChirp(forms.ModelForm):
    class Meta:
        model = Chirp
        fields = [
            'message',
            'user'
            ]