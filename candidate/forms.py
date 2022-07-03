from django import forms
from candidate.models import CandidateProfileModel

class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model=CandidateProfileModel
        exclude=("user",)