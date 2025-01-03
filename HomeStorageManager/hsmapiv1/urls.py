from django.urls import include, path
from rest_framework import routers
from hsmapiv1 import views

"""
Verwendung der Funktion routers des Rest Frameworks um die
URL Pattern zu erstellen ebenso wie das hinzufügen der Authentifizierung URLs.
"""

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'units', views.UnitViewSet)
router.register(r'objects', views.ObjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]