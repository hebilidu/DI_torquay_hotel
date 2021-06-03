from django import forms

ROOM_TYPE_CHOICES = (
    ("1", "2 persons"),
    ("2", "4 persons"),
    ("3", "Suite")
)

class FamilyForm(forms.Form):
    start_date = forms.DateField()
    end_date = forms.DateField()
    room_type = forms.ChoiceField(choices = ROOM_TYPE_CHOICES)