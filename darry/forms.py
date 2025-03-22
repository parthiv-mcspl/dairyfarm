from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'message', 'rating']
        widgets = {
            'rating': forms.RadioSelect(choices=[(i, f"{i} Stars") for i in range(1, 6)]),
        }
