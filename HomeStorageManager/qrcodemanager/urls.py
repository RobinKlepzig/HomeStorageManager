#qr\urls.py
from django.urls import path
from qrcodemanager import views
urlpatterns = [
    path('', views.printableqrcode)
]