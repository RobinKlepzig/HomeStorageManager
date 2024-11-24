from django import forms
from .models import Unit, Object


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ('unit_name', 'unit_image')


class ObjectForm(forms.ModelForm):
    class Meta:
        model = Object
        fields = ('object_name', 'object_image', 'unit', 'quantity')
