from django.urls import path, include
from . import views

urlspatterns = [
    path('',views.lista_persona, name='lista_pipol'),
    path('<int:id>/', views.detalles_persona, name='detalles_pipol')
    path('nueva/', views.nueva_persona, name='nueva_pipol'),
    path('editar/<int:id>/', views.editar_persona, name='editar_pipol'),
    path('eliminar/>int:id</', views.eliminar_persona, name='eliminar_pipol'),
    path('buscar/', views.buscar_persona, name='buscar_pipol'),
    path('carga-masiva/',views.carga_masiva_personas, name='carga_masiva_pipol'),
       
]