from django import forms
from movieapp.models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'description', 'year', 'image', 'image2']