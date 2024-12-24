from django import forms
from.models import Patients1

# form الطريقة الثانية إنشاء
class PatientsForm(forms.ModelForm):
    first_name = forms.CharField(label="First Name", widget=forms.TextInput(), required=True, initial='patients',help_text="This Is The First Name")
    second_name = forms.CharField(label="Second Name", widget=forms.TextInput(), required=True, initial='patients',help_text="This Is The Second Name")
    age = forms.IntegerField(label="age", widget=forms.NumberInput(), required=True, initial='20')
    image = forms.ImageField(label="Image", widget=forms.FileInput())
    file_report = forms.FileField(label="file report", widget=forms.FileInput())
    report = forms.CharField(label='report', widget=forms.Textarea())
    class Meta:
        model = Patients1 # تأكد من أنك تستخدم النموذج الصحيح 
        fields = ['first_name', 'second_name', 'age', 'image', 'file_report', 'report']