## factories.py
import factory
from factory.django import DjangoModelFactory

from main.models import *

## Defining a factory

# OSAM KRVNIH GRUPA
class KrvnaGrupa0plusFactory(DjangoModelFactory):
    class Meta:
        model = KrvnaGrupa
    antigen = '0'
    RhFaktor = '+'
class KrvnaGrupa0minusFactory(DjangoModelFactory):
    class Meta:
        model = KrvnaGrupa
    antigen = '0'
    RhFaktor = '-'
class KrvnaGrupaAplusFactory(DjangoModelFactory):
    class Meta:
        model = KrvnaGrupa
    antigen = 'A'
    RhFaktor = '+'
class KrvnaGrupaAminusFactory(DjangoModelFactory):
    class Meta:
        model = KrvnaGrupa
    antigen = 'A'
    RhFaktor = '-'
class KrvnaGrupaBplusFactory(DjangoModelFactory):
    class Meta:
        model = KrvnaGrupa
    antigen = 'B'
    RhFaktor = '+'
class KrvnaGrupaBminusFactory(DjangoModelFactory):
    class Meta:
        model = KrvnaGrupa
    antigen = 'B'
    RhFaktor = '-'
class KrvnaGrupaABplusFactory(DjangoModelFactory):
    class Meta:
        model = KrvnaGrupa
    antigen = 'AB'
    RhFaktor = '+'
class KrvnaGrupaABminusFactory(DjangoModelFactory):
    class Meta:
        model = KrvnaGrupa
    antigen = 'AB'
    RhFaktor = '-'

'''
class SpremnikKrviFactory(DjangoModelFactory):
    class Meta:
        model = SpremnikKrvi
    krvna_grupa = factory.Faker(KrvnaGrupa) # izmisli smo kod
'''

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
    prezime = models.CharField("last_name")
    krvna_grupa = factory.Iterator(KrvnaGrupa.objects.all())
    
'''
class DonacijaFactory(DjangoModelFactory):
    class Meta:
        model = Donacija

    vrijeme = factory.Faker("date_time")
'''
