from django.db import models
from django.utils import timezone

# Create your models here.
class KrvnaGrupa(models.Model):
    # odabiri antigena
    kg = models.CharField(max_length=3, default=None)
    '''
    nula = '0'
    a = 'A'
    b = 'B'
    ab = 'AB'
    antigeni = [
        (nula, '0'),
        (a, 'A'),
        (b, 'B'),
        (ab, 'AB'),
    ]
    antigen = models.CharField(
        max_length=2,
        choices=antigeni,
        default=nula,
    )
    # odabiri Rh faktora
    plus = '+'
    minus = '-'
    RhFaktori = [
        (plus, '+'),
        (minus, '-'),
    ]
    RhFaktor = models.CharField(
        max_length=1,
        choices=RhFaktori,
        default=plus,
    )
    '''
    def __str__(self):
        return self.kg # self.antigen + self.RhFaktor

class SpremnikKrvi(models.Model):
    krvna_grupa = models.ManyToManyField(KrvnaGrupa)
    # br_donacija = 0
    # br_primanja = 0
    # br_l_krvi = 5
    def __str__(self):
        return str(self.pk) + '-' + str(self.krvna_grupa) #  + str(self.br_l_krvi) + 'L'

class Donator(models.Model):
    ime = models.CharField(max_length=64)
    prezime = models.CharField(max_length=64)
    krvna_grupa = models.ForeignKey(KrvnaGrupa, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.ime + self.prezime

class Primatelj(models.Model):
    ime = models.CharField(max_length=64)
    prezime = models.CharField(max_length=64)
    krvna_grupa = models.ForeignKey(KrvnaGrupa, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.ime + ' ' + self.prezime

class Donacija(models.Model):
    vrijeme_transakcije = models.DateTimeField(default=timezone.now)

    donator = models.OneToOneField(
        Donator,
        on_delete=models.CASCADE,
        primary_key=True,
        default=None,
    )
    spremnik_krvi = models.OneToOneField(
        SpremnikKrvi,
        on_delete=models.CASCADE,
        default=None,
    )
    '''
    SpremnikKrvi.br_donacija = SpremnikKrvi.br_donacija + 1
    SpremnikKrvi.br_l_krvi = SpremnikKrvi.br_donacija - SpremnikKrvi.br_primanja
    '''
    # litraza = models.IntegerField(default=1)
    def __str__(self):
        return str(self.pk) + '_' + str(self.vrijeme_transakcije) + '_' + str(self.donator.krvna_grupa)

class Primanje(models.Model):
    primatelj = models.ForeignKey(Primatelj, on_delete=models.CASCADE, default=None)
    spremnik_krvi = models.ForeignKey(SpremnikKrvi, on_delete=models.CASCADE, default=None)
    '''
    SpremnikKrvi.br_primanja = SpremnikKrvi.br_primanja + 1
    SpremnikKrvi.br_l_krvi = SpremnikKrvi.br_donacija - SpremnikKrvi.br_primanja
    '''
    # litraza = models.IntegerField(default=1)
    def __str__(self):
        return str(self.pk)

class DonacijskaKartica(models.Model):
    donator = models.OneToOneField(
        Donator,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    def __str__(self):
        return str(self.pk) + '_' +  str(self.donator.ime) + str(self.donator.prezime)
