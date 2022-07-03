from django import forms
from employer.models import EmployeeProfile,Jobs
class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model=EmployeeProfile
        # fields=["company_name",
        #         "logo",
        #         "bio",
        #         "location",
        #         "services"
        #         ]
        exclude = ("user",)

class JobForm(forms.ModelForm):
    class Meta:
        model=Jobs
        exclude=("posted_by","created_date",)
        widgets={
            "last_date":forms.DateInput(attrs={"class":"form-control","type":"date"})
        }

class JobUpdateForm(forms.ModelForm):
    class Meta:
        model=Jobs
        exclude = ("posted_by", "created_date","last_date")
