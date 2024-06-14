from django.urls import path

from idpets import settings
from . import views
from django.conf.urls.static import static



urlpatterns = [
    path('inicio', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('Mascotas', views.lista_mascotas, name='Mascotas'),
    path('registrar_mascota', views.registrar_mascota, name='registrar_mascota'),
    path('editar_mascotas', views.editar_mascotas, name='editar_mascotas'),
    path('signup', views.signup, name='signup'),
    path('', views.iniciar_sesion, name='login'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('editar_usuario/', views.editar_usuario, name='editar_usuario'),
    path('borrar/', views.borrar_usuario, name='borrar_usuario'),
    path('detalle/<int:mascota_id>/', views.detalle_mascota, name='detalle_mascota'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)