from django.core.exceptions import ValidationError
from django import forms


class CreateReview(forms.Form):
    rating = forms.IntegerField(
        label="Rating",
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Rate the product from 1 to 5",
            }
        ),
    )
    comment = forms.CharField(
        label="Comment",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Write your review here",
                "rows": 4,
            }
        ),
    )

