from django import  forms
from django.core.exceptions import ValidationError
from django.template.defaultfilters import first

class NoteForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    CATEGORY_CHOICES = [
        ("Personal", "Personal"),
        ("Work", "Work"),
        ("Study", "Study"),
    ]
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    tags = forms.CharField(max_length=100, required=False)

    def clean_title(self):
        title = self.cleaned_data['title'].strip()
        banned_words = ["test"]
        if any(word in title.lower() for word in banned_words):
            raise ValidationError("Title contains banned words")
        return title