from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("storagemanager.urls")),
    path("qr-code/", include("qrcodemanager.urls")),
    path('accounts/', include('allauth.urls')),
    path("apiv1/", include('hsmapiv1.urls')),
    path("admin/", admin.site.urls),
]
