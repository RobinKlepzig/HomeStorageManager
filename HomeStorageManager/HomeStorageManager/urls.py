from django.contrib import admin
from django.urls import include, path

"""
Genereller Einbezug des URL Files der Haupt-App, falls
kein expliziertes Verzeichnis angegeben wird.
Folgend werden dann auf die weiteren URL Files
der Apps zu den URL-Pattern hinzugefügt.
"""

urlpatterns = [
    path("", include("storagemanager.urls")),
    path("qr-code/", include("qrcodemanager.urls")),
    path("accounts/", include("allauth.urls")),
    path("apiv1/", include('hsmapiv1.urls')),
    path("admin/", admin.site.urls),
]
