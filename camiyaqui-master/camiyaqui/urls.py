from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

urlpatterns = [
    path('', include('ourwedding.urls')),
    path('admin/', admin.site.urls),
    path('backend/', include('backend.urls')),
    path('logout', LogoutView.as_view(), name='logout'),
    path('api/', include('api.urls')),
    path('photos/', include('photos.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
