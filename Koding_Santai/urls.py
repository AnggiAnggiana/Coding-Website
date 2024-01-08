from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('kelas_programming.urls')),
    path('admin/', admin.site.urls),
    path('akses/', include('django.contrib.auth.urls')),
    path('akses/', include('akses.urls')),
    path('accounts/', include('allauth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

