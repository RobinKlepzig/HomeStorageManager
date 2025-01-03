from django.urls import path
from qrcodemanager import views

"""
Alle Aufrufe werden an die Funktion views.printableqrcode geroutet.
"""

urlpatterns = [
    path('', views.printableqrcode)
]