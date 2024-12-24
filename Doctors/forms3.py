from django import forms
from .models import Doctors

class DoctorsForm(forms.ModelForm):
    class Meta:
        model=Doctors 
        # _fields='_all
        fields=['first_name', 'last_name', 'age', 'report']