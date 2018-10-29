from django.conf.urls import url
from . import views #importar views del directorio actual
from django.conf import settings
from django.conf.urls.static import static
from perros.views import lista_rescate

urlpatterns = [
    url(r'^$',views.formularioperro, name='servicios'),
    url(r'^ver$',lista_rescate, name='ver'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        