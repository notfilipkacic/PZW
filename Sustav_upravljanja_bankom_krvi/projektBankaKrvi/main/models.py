from django.db import models
from django.utils import timezone

# Create your models here.
class KrvnaGrupa(models.Model):
    # odabiri antigena
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
    def __str__(self):
        return self.antigen + self.RhFaktor

class Donator(models.Model):
    ime = models.CharField(max_length=64)
    prezime = models.CharField(max_length=64)

    # krvna_grupa = models.ForeignKey(KrvnaGrupa, on_delete=models.CASCADE)

    def __str__(self):
        return self.ime + self.prezime

class Primatelj(models.Model):
    ime = models.CharField(max_length=64)
    prezime = models.CharField(max_length=64)

    # krvna_grupa = models.ForeignKey(KrvnaGrupa, on_delete=models.CASCADE)

    def __str__(self):
        return self.ime + ' ' + self.prezime

class Donacija(models.Model):
    vrijeme_transakcije = models.DateTimeField(default=timezone.now)

    # donator = models.ForeignKey(Donator, on_delete=models.CASCADE)

    litraza = models.FloatField(default=0.5)

    def __str__(self):
        return str(self.litraza)

class Primanje(models.Model):

    # donator = models.ForeignKey(Primatelj, on_delete=models.CASCADE)

    litraza = models.FloatField(default=0.5)

    def __str__(self):
        return str(self.litraza)