from . import views
from django.urls import path

app_name = 'Patients'
urlpatterns = [
    path('',views.home, name="home"),
    path('create/',views.patients_create, name="create"),
    path('show/', views.all_patients, name="show"),
    path('success/', views.success_message, name="success_message"),
    path('error/', views.error_page, name="error_page"),
    path('show/<int:pk>', views.patient_show_detail, name="showdetail"),
    path('update/<int:pk>', views.patient_edit, name="edit"),
    path('delete/<int:pk>', views.delete_patient, name="delete"),
    path('forms/', views.show_forms, name="forms"),
]

