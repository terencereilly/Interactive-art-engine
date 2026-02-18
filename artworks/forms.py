from django import forms

class CreateInstanceForm(forms.Form):
    TEMPLATE_CHOICES = [
        ("1A", "Artwork 1A"),
        ("1B", "Artwork 1B"),
    ]
    template = forms.ChoiceField(choices=TEMPLATE_CHOICES, label="Artwork Template")
    duration_days = forms.IntegerField(min_value=1, max_value=365, initial=30, label="License Duration (days)")
