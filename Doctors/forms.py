from django import forms
from .models import Doctors

# form الطريقة الثانية إنشاء
class DoctorsForm(forms.ModelForm):
    first_name = forms.CharField(label="First Name", widget=forms.TextInput(), required=True, initial='doctors',help_text="This Is The First Name")
    second_name = forms.CharField(label="Second Name", widget=forms.TextInput(), required=True, initial='doctors',help_text="This Is The Second Name")
    age = forms.IntegerField(label="age", widget=forms.NumberInput(), required=True, initial='20')
    specialization = forms.CharField(label="specializ", widget=forms.TextInput(), required=True, initial="specialization", help_text="the specialization")
    mattress = forms.CharField(label="matt", widget=forms.TextInput(), required=True, initial="the mattrers", help_text="write the mattress")
    image = forms.ImageField(label="Image", widget=forms.FileInput())
    file_report = forms.FileField(label="file report", widget=forms.FileInput())
    report = forms.CharField(label='report', widget=forms.Textarea())
    class Meta:
        model = Doctors # تأكد من أنك تستخدم النموذج الصحيح 
        fields = ['first_name', 'second_name', 'age', 'specialization', 'mattress', 'image', 'file_report', 'report']