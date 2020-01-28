from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('introducao', views.introducao, name='introducao'),
    path('colecoes', views.colecoes, name='colecoes'),
    path('especie/<int:id>', views.especie, name='especie'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)