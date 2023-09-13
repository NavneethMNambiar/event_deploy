from django import forms
from .models import Participant

class Participantform(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['participant_name','participant_id','participant_phone']

