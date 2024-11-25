"""
URL configuration for storagemanager app.
"""
from django.urls import path
from storagemanager.views import units, objects, unit, object, newunit, newobject, deleteobject, deleteunit

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", units, name='home'),
    path("units/", units, name='units'),
    path("unit/<int:unit_id>/", unit, name='unit'),
    path("unit/new/", newunit, name='newunit'),
    path("unit/delete/<int:unit_id>/", deleteunit, name='deleteunit'),
    path("objects/", objects, name='objects'),
    path("object/<int:object_id>/", object, name='object'),
    path("object/new/", newobject, name='newobject'),
    path("object/delete/<int:object_id>/", deleteobject, name='deleteobject'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
