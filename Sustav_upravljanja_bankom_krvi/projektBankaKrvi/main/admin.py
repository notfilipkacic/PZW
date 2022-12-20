from django.contrib import admin
from .models import *

# Register your models here.

model_list = [KrvnaGrupa, Donator, Primatelj, Donacija, Primanje]
admin.site.register(model_list)