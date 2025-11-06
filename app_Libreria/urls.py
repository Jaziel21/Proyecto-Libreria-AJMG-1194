from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_libreria, name='inicio_libreria'),
    path('autores/agregar/', views.agregar_autor, name='agregar_autor'),
    path('autores/', views.ver_autores, name='ver_autores'),
    path('autores/editar/<int:autor_id>/', views.actualizar_autor, name='actualizar_autor'),
    path('autores/editar/guardar/<int:autor_id>/', views.realizar_actualizacion_autor, name='realizar_actualizacion_autor'),
    path('autores/borrar/<int:autor_id>/', views.borrar_autor, name='borrar_autor'),
]