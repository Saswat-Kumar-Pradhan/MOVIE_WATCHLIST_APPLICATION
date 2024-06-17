from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'release_year', 'genre', 'watched', 'rating', 'review']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'release_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'watched': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'rating': forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 6)], attrs={'class': 'form-check-input'}),
            'review': forms.Textarea(attrs={'class': 'form-control'}),
        }
