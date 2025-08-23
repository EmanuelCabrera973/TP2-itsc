from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.lista_oficina, name='lista_oficina'),
    path('nueva/',views.nueva_oficina, name='nueva_oficina'),
    path('<int:id>/',views.detalle_oficina, name='detalles_oficina'),
    path('editar/<int:id>/', views.editar_oficina, name='editar_oficina'),
    path('eliminar/<int:id>/', views.eliminar_oficina, name='eliminar_oficina'),
    path('buscar/', views.buscar_oficina, name='buscar_oficina'),
    path('carga_masiva/', views.carga_masiva, name='carga_masiva_oficina'),
    
]