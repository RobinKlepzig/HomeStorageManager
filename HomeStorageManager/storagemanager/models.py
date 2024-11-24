from django.db import models
from django.contrib.auth.models import User


class Unit(models.Model):
    unit_name = models.CharField(max_length=128)
    unit_image = models.ImageField(upload_to='images/', default='images/box-open.svg')
    create_date = models.DateTimeField(auto_now_add=True)
    lastmodified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.unit_name


class Object(models.Model):
    object_name = models.CharField(max_length=128)
    object_image = models.ImageField(upload_to='images/', default='images/item.svg')
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    create_date = models.DateTimeField(auto_now_add=True)
    lastmodified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.object_name
