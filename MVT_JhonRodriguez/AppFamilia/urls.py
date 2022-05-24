from django.urls import path
from AppFamilia.views import cargarFamilia, datosFamilia

urlpatterns = [
    
    path('cargar/<nombre>/<int:edad>/<fecha>',cargarFamilia),
    path('familiares', datosFamilia)
]