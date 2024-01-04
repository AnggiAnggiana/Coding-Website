from django.contrib import admin
from django.urls import path, include
# part 2 form profile image
# part 3 di file models.py folder aplikasi(kelas_programming)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('kelas_programming.urls')),
    path('admin/', admin.site.urls),
    path('akses/', include('django.contrib.auth.urls')),
    path('akses/', include('akses.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

