from django.contrib import admin
from .models import *

model_list = [KrvnaGrupa, Donator, Primatelj, Donacija, Primanje, SpremnikKrvi, DonacijskaKartica]


# Register your models here.
admin.site.register(model_list)