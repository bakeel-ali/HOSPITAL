from django.contrib import admin

# Register your models here.
from .models import Doctors
admin.site.register(Doctors)

admin.site.site_header = 'H.P.S'
admin.site.site_title = 'H.P.S'

# SjangpSuit with link

# in layout ==> apps.py

# grappille them 