from django import forms
from testapp.models import Rating


class RatingForm(forms.ModelForm):
    class Meta:
        model=Rating
        fields=('restaurant','user','rating')