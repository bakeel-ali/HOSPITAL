from django.db import models

# Create your models here.
class Doctors(models.Model):
    first_name = models.CharField(max_length=33, default="Unknown")
    last_name = models.CharField(max_length=33, default="Unknown")
    age = models.PositiveIntegerField(default=18)
    specialization = models.CharField(max_length=20, default="UnKnown")
    mattress = models.CharField(max_length=12, default="UnKnown")
    image = models.ImageField(upload_to='Doctors/images/%y/%m/%d', null=True)
    file_report = models.FileField(upload_to='Doctors/files/%y/%m/%d', null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)
    report = models.TextField(max_length=200)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
