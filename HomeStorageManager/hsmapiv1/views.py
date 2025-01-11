from django.contrib.auth.models import Group, User
from storagemanager.models import Unit, Object
from rest_framework import permissions, viewsets

from hsmapiv1.serializers import GroupSerializer, UserSerializer, UnitSerializer, ObjectSerializer

'''
API-Endpunkte für verschiedene Datenmodelle. 
Dabei werden die Modelle User, Group, Unit und Object das ViewSet beschrieben.
'''

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all().order_by('unit_name')
    serializer_class = UnitSerializer
    permission_classes = [permissions.IsAuthenticated]


class ObjectViewSet(viewsets.ModelViewSet):
    queryset = Object.objects.all().order_by('object_name')
    serializer_class = ObjectSerializer
    permission_classes = [permissions.IsAuthenticated]
