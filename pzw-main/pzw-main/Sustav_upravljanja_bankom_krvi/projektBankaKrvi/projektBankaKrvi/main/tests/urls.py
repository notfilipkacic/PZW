from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import hello_world, Mosquito, DonacijeList, KarticeList, DonatoriList, KrvnaGrupaList,PrimateljList,SpremnikKrviList, PrimanjeList


class TestUrls(SimpleTestCase):

    def test_hello_world_url_is_resolved(self):
        url = reverse('')
        # print(resolve(url))

        self.assertEquals(resolve(url).func, hello_world)

    def test_books_url_is_resolved(self):
        url = reverse('izbornik')

        self.assertEquals(resolve(url).func.view_class, Mosquito)

    def test_authors_url_is_resolved(self):
        url = reverse('donacija')

        self.assertEquals(resolve(url).func.view_class, DonacijeList)

    def test_authors_url_is_resolved(self):
        url = reverse('donacijskakartica')

        self.assertEquals(resolve(url).func.view_class, KarticeList)
    
    def test_authors_url_is_resolved(self):
        url = reverse('donator', args=['some-author'])

        self.assertEquals(resolve(url).func.view_class, DonatoriList)
    
    def test_authors_url_is_resolved(self):
        url = reverse('krvnagrupa')

        self.assertEquals(resolve(url).func.view_class, KrvnaGrupaList)
    
    def test_authors_url_is_resolved(self):
        url = reverse('primatelj')

        self.assertEquals(resolve(url).func.view_class, PrimateljList)

    def test_authors_url_is_resolved(self):
        url = reverse('spremnikkrvi')

        self.assertEquals(resolve(url).func.view_class, SpremnikKrviList)

    def test_authors_url_is_resolved(self):
        url = reverse('primanje')

        self.assertEquals(resolve(url).func.view_class, PrimanjeList)
