from . import views
from django.urls import path

app_name = 'Doctors'
urlpatterns = [
    path('',views.Dhome, name="home"),
    path('create/',views.doctors_create, name="create"),
    path('show/', views.all_doctors, name="show"),
    path('success/', views.success_message, name="success_message"),
    path('error/', views.error_page, name="error_page"),
    path('show/<int:pk>', views.doctor_show_detail, name="showdetail"),
    path('update/<int:pk>', views.doctor_edit, name="edit"),
    path('delete/<int:pk>', views.delete_doctor, name="delete"),
    path('forms/', views.show_forms, name="forms"),
]

