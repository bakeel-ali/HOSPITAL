import os
from sqlite3 import IntegrityError
# from django import forms
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import PatientsForm
from .models import Patients1

# Create your views here.
def home(request):
    return render(request, 'Patients/P_home.html')

def all_patients(request):
    patients = Patients1.objects.all()
    if patients.exists:
        return render(request, 'Patients/all_patients.html', {'patients':patients})
    else:
        return redirect(reverse('Patients:error_page'))
    
def success_message(request):
    return render(request, 'Patients/success_message.html')

def error_page(request):
    return render(request, 'Patients/error_page.html')

# 1111111
    # HttpResponse('pk',pk)
    # print('pk=',pk)
def patient_show_detail(request,pk):
    # pk = 4
    patientss = Patients1.objects.get(id=pk)    
    try:
        return render(request, 'Patients/patient_info.html',{"patientss":patientss})
    except:
        return redirect(reverse('Patients:error_page'))
    
def delete_patient(request,pk):
    try:
        patient = get_object_or_404(Patients1, pk=pk)
        if patient.image :
            image_path = patient.image.path
            if os.path.isfile(image_path):
                os.remove(image_path)
        if patient.file_report:
            file_report_path = patient.file_report.path
            if os.path.isfile(file_report_path):
                os.remove(file_report_path)
        patient.delete()
        return redirect(reverse('Patients:success_message'))
    except:
        return redirect(reverse('Patients:error_page'))
    
def patients_create(request):
    if request.method == 'POST':
        try:
            patient = Patients1.objects.create(
                first_name=request.POST.get('fname'),
                last_name=request.POST.get('lname'),
                age=request.POST.get('age'),
                report=request.POST.get('report'),
                image=request.FILES.get('image'),
                file_report=request.FILES.get('medicalreport')
            )
            return redirect(reverse('Patients:success_message'))
        except IntegrityError:
            return redirect(reverse('Patients:error_page'))
    else:
        return render(request, 'Patients/patient_create.html')    
    
def patient_edit(request, pk):
    patient = get_object_or_404(Patients1, pk=pk)
    if request.method == 'POST':
        try:
            patient.first_name = request.POST.get('fname')
            patient.last_name = request.POST.get('lname')
            patient.age = request.POST.get('age')
            patient.report = request.POST.get('report')
            patient.image=request.FILES.get('image')
            patient.file_report=request.FILES.get('medicalreport')
            patient.save()
            return redirect(reverse('Patients:success_message'))
        except IntegrityError:
            return redirect(reverse('Patients:error_page'))
    else:
        return render(request, 'Patients/patient_update.html',{'patient': patient})
   
#هذه الدالة للطريقتين الاخيرتين من طرق انشاء الفورم مع الطريقة الاولى طبعا
# from .forms import forms   #forms3.py
def show_forms(request):
    if request.method == 'POST':
        patient_form = PatientsForm (request.POST, request.FILES)
        if patient_form.is_valid():
            patient_form.save()
            return HttpResponse('Created')
        else:
            return HttpResponse('Field!!')
    else:
        patient_form = PatientsForm()
        return render(request, 'Patients/other_type_forms.html', {'form': PatientsForm})