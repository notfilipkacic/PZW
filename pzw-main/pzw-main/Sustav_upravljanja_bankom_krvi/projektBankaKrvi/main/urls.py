from django.urls import path
from . import views

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('', views.hello_world, name='Hello world!'),
    path('donacija', views.DonacijeList.as_view()), # ne radi jer je primary
    path('donacijskakartica', views.KarticeList.as_view()), # ne radi jer je primary
    path('donator', views.DonatoriList.as_view()),
    path('krvnagrupa', views.KrvnaGrupaList.as_view()),
    path('primatelj', views.PrimateljList.as_view()),
    path('spremnikkrvi', views.SpremnikKrviList.as_view()), # ne radi jer je primary
    path('primanje', views.PrimanjeList.as_view()), # ne radi jer je m2m veza
    path('izbornik', views.Mosquito.as_view()),
]