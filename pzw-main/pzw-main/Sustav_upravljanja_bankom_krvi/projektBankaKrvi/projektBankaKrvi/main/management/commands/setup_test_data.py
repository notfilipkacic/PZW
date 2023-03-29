import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import *
from main.factory import *
'''
(
    KrvnaGrupa0plusFactory,
    KrvnaGrupa0minusFactory,
    KrvnaGrupaAplusFactory,
    KrvnaGrupaAminusFactory,
    KrvnaGrupaBplusFactory,
    KrvnaGrupaBminusFactory,
    KrvnaGrupaABplusFactory,
    KrvnaGrupaABminusFactory,
    # SpremnikKrviFactory,
    DonatorFactory,
    PrimateljFactory,
)
'''
NUM_SPREMNIKS = 32
NUM_DONATORS = 128
NUM_PRIMATELJS = 64
NUM_DONACIJAS = 256
NUM_PRIMANJAS = 128
NUM_DONACIJSKA_KARTICAS = 128

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [KrvnaGrupa, Donator, Primatelj, Donacija, Primanje, SpremnikKrvi, DonacijskaKartica]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        prva = KrvnaGrupa0plusFactory()
        druga = KrvnaGrupa0minusFactory()
        treca = KrvnaGrupaAplusFactory()
        cetvrta = KrvnaGrupaAminusFactory()
        peta  = KrvnaGrupaBplusFactory()
        sesta = KrvnaGrupaBminusFactory()
        sedma = KrvnaGrupaABplusFactory()
        osma = KrvnaGrupaABminusFactory()
        
        for _ in range(NUM_DONATORS):
            donator = DonatorFactory()

        for _ in range(NUM_PRIMATELJS):
            primatelj = PrimateljFactory()

        '''
        for _ in range(NUM_SPREMNIKS):
            spremnik = SpremnikKrviFactory()()
        '''        
        '''
        for _ in range(NUM_DONACIJAS):
            donacija = DonacijaFactory()
        '''
        '''
        for _ in range(NUM_PRIMANJAS):
            primanje = PrimanjeFactory()
        '''
        '''
        for _ in range(NUM_DONACIJSKA_KARTICAS):
            kartica = DonacijskaKarticaFactory()
        '''