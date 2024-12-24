import os
from sqlite3 import IntegrityError
# from django import forms
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import DoctorsForm
from .models import Doctors

# Create your views here.
def Dhome(request):
    return render(request, 'Doctors/D_home.html')

def all_doctors(request):
    doctors = Doctors.objects.all()
    if doctors.exists:
        return render(request, 'Doctors/all_doctors.html', {'doctors':doctors})
    else:
        return redirect(reverse('Doctors:error_page'))
    
def success_message(request):
    return render(request, 'Doctors/success_message.html')

def error_page(request):
    return render(request, 'Doctors/error_page.html')

# 1111111
    # HttpResponse('pk',pk)
    # print('pk=',pk)
    # pk = 4
def doctor_show_detail(request,pk):
    doctors = Doctors.objects.get(id=pk)    
    try:
        return render(request, 'Doctors/doctor_info.html',{"doctors":doctors})
    except:
        return redirect(reverse('Doctors:error_page'))
    
def delete_doctor(request,pk):
    try:
        doctor = get_object_or_404(Doctors, pk=pk)
        image_old = doctor.image.path
        if image_old :
            # image_path = doctor.image.path
            try:
                os.remove(image_old)  # حذف الصورة القديمة
            except Exception as e:
                print(f"Error deleting old image: {e}")  # طباعة الخطأ إذا حدث
        file_old = doctor.file_report.path
        if file_old:
            # file_report_path = doctor.file_report.path
            try:
                os.remove(file_old)  # حذف الملف القديم
            except Exception as e:
                print(f"Error deleting old file: {e}")  # طباعة الخطأ إذا حدث
        doctor.delete()
        return redirect(reverse('Doctors:success_message'))
    except:
        return redirect(reverse('Doctors:error_page'))
    
def doctors_create(request):
    if request.method == 'POST':
        try:
            doctors = Doctors.objects.create(
                first_name=request.POST.get('fname'),
                last_name=request.POST.get('lname'),
                specialization = request.POST.get('specializ'),
                mattress = request.POST.get('matt'),
                age=request.POST.get('age'),
                report=request.POST.get('report'),
                image=request.FILES.get('image'),
                file_report=request.FILES.get('medicalreport')
            )
            return redirect(reverse('Doctors:success_message'))
        except IntegrityError:
            return redirect(reverse('Doctors:error_page'))
    else:
        return render(request, 'Doctors/doctor_create.html')    
    
def doctor_edit(request, pk):
    doctor = get_object_or_404(Doctors, pk=pk)
    if request.method == 'POST':
        try:
            doctor.first_name = request.POST.get('fname')
            doctor.last_name = request.POST.get('lname')
            doctor.age = request.POST.get('age')
            doctor.specialization = request.POST.get('specializ')
            doctor.mattress = request.POST.get('matt')
            doctor.report = request.POST.get('report')
            new_image = request.FILES.get('image')
            if new_image:
                # إذا كان هناك صورة جديدة، احفظ المسار القديم
                if doctor.image:
                    old_image_path = doctor.image.path  # الحصول على المسار القديم
                    try:
                        os.remove(old_image_path)  # حذف الصورة القديمة
                    except Exception as e:
                        print(f"Error deleting old image: {e}")  # طباعة الخطأ إذا حدث
                doctor.image = new_image
            doctor.image=new_image
            new_file_repotr= request.FILES.get('medicalreport')
            if new_file_repotr:
                if doctor.file_report:
                    odl_path = doctor.file_report.path
                    try:
                        os.remove(odl_path)
                    except Exception as e:
                        print(f"eror to reblase a file: {e}")
                doctor.file_report = new_file_repotr            
            # doctor.file_report=request.FILES.get('medicalreport')
            doctor.save()
            return redirect(reverse('Doctors:success_message'))
        except IntegrityError:
            return redirect(reverse('Doctors:error_page'))
    else:
        return render(request, 'Doctors/doctor_update.html',{'doctor': doctor})
   
#هذه الدالة للطريقتين الاخيرتين من طرق انشاء الفورم مع الطريقة الاولى طبعا
# from .forms import forms   #forms3.py
def show_forms(request):
    if request.method == 'POST':
        doctor_form = DoctorsForm (request.POST, request.FILES)
        if doctor_form.is_valid():
            doctor_form.save()
            return HttpResponse('Created')
        else:
            return HttpResponse('Field!!')
    else:
        doctor_form = DoctorsForm()
        return render(request, 'Doctors/other_type_forms.html', {'form': DoctorsForm})