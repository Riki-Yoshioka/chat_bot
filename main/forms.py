from django import forms
from .models import Dialogue


class TalkForm(forms.ModelForm):
    class Meta:
        model = Dialogue
        fields = ("message",)
        # labels = {"message":"",}