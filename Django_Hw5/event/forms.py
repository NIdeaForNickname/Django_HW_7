from django import forms
from django.forms import formset_factory

class EventForm(forms.Form):
    name = forms.CharField(label="Event name")
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

class ParticipantForm(forms.Form):
    email = forms.EmailField(label="Participant email")
