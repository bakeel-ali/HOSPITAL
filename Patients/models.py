from django.db import models

# Create your models here.
class Patients1(models.Model):
    first_name = models.CharField(max_length=33, default="Unkown")
    last_name = models.CharField(max_length=33, default="Unkown")
    age = models.PositiveIntegerField(default=18)
    image = models.ImageField(upload_to='images/%y/%m/%d', null=True)
    file_report = models.FileField(upload_to='files/%y/%m/%d', null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)
    report = models.TextField(max_length=200)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
