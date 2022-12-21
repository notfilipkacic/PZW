## factories.py
import factory
from factory.django import DjangoModelFactory

from main.models import *

## Defining a factory

# OSAM KRVNIH GRUPA
class KrvnaGrupa0plusFactory(DjangoModelFactory):   
    class Meta:
        model = KrvnaGrupa
    kg = '0+'
class KrvnaGrupa0minusFactory(DjangoModelFactory):
    class Meta:
        model = KrvnaGrupa
    kg = '0-'
class KrvnaGrupaAplusFactory(DjangoModelFactory):
    class Meta:
        model = KrvnaGrupa
    kg = 'A+'
class KrvnaGrupaAminusFactory(DjangoModelFactory):
    class Meta:
        model = KrvnaGrupa
    kg = 'A-'
class KrvnaGrupaBplusFactory(DjangoModelFactory):
    class Meta:
        model = KrvnaGrupa
    kg = 'B+'
class KrvnaGrupaBminusFactory(DjangoModelFactory):
    class Meta:
        model = KrvnaGrupa
    kg = 'B-'
class KrvnaGrupaABplusFactory(DjangoModelFactory):
    class Meta:
        model = KrvnaGrupa
    kg = 'AB+'
class KrvnaGrupaABminusFactory(DjangoModelFactory):
    class Meta:
        model = KrvnaGrupa
    kg = 'AB-'

class SpremnikKrviFactory(DjangoModelFactory):
    class Meta:
        model = SpremnikKrvi
    krvna_grupa = factory.SubFactory(KrvnaGrupa) # m2m field factory ??


class DonatorFactory(DjangoModelFactory):
    class Meta:
        model = Donator
    ime = factory.Faker("first_name")
    prezime = factory.Faker("last_name")
    krvna_grupa = factory.Iterator(KrvnaGrupa.objects.all())
    
class PrimateljFactory(DjangoModelFactory):
    class Meta:
        model = Primatelj
    ime = factory.Faker("first_name")
    prezime = factory.Faker("last_name")
    krvna_grupa = factory.Iterator(KrvnaGrupa.objects.all())

'''
class DonacijaFactory(DjangoModelFactory):
    class Meta:
        model = Donacija

    vrijeme = factory.Faker("date_time")
'''