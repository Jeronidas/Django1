from django.urls import path
from inicio.views import mi_vista, inicio

urlpatterns = [
    path('mi-vista/', mi_vista),
    path('', inicio)
]
