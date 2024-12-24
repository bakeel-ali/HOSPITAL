from django import forms
from .models import Patients1

class PatientsForm(forms.ModelForm):
    class Meta:
        model=Patients1 
        # _fields='_all
        fields=['first_name', 'last_name', 'age', 'report']