from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Unit, Object
from .forms import UnitForm, ObjectForm
from django.contrib import messages


def units(request):
    latest_units_list = Unit.objects.order_by("create_date")[:100]
    context = {"latest_units_list": latest_units_list}
    return render(request, "storagemanager/units.html", context)


def unit(request, unit_id):
    try:
        unit = get_object_or_404(Unit, pk=unit_id)
    except Unit.DoesNotExist:
        raise Http404("Unit does not exist")

    objects = Object.objects.filter(unit=unit_id)

    return render(request, "storagemanager/unit.html", {"unit": unit, "objects": objects})


def newunit(request):
    form = UnitForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            if not obj.created_by:
                obj.created_by = request.user
            obj.save()
            messages.success(request, "Unit successfully created", "alert-success alert-dismissible")
            #Object.objects.all().delete()
        else:
            print(form.errors)

    context = {
        'form': form
    }

    return render(request, "storagemanager/newunit.html", context)


def deleteunit(request, unit_id):
    try:
        unit = get_object_or_404(Unit, pk=unit_id)
    except Object.DoesNotExist:
        raise Http404("Unit does not exist")
    unit.delete()

    latest_units_list = Unit.objects.order_by("create_date")[:1000000]
    context = {"latest_units_list": latest_units_list}

    return render(request, "storagemanager/units.html", context)


def objects(request):
    latest_objects_list = Object.objects.order_by("create_date")[:100]
    context = {"latest_objects_list": latest_objects_list}
    return render(request, "storagemanager/objects.html", context)


def object(request, object_id):
    try:
        object = get_object_or_404(Object, pk=object_id)
    except Object.DoesNotExist:
        raise Http404("Object does not exist")

    return render(request, "storagemanager/object.html", {"object": object})


def newobject(request):
    form = ObjectForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            if not obj.created_by:
                obj.created_by = request.user
            obj.save()
            messages.success(request, "Object successfully created", "alert-success alert-dismissible")
        else:
            print(form.errors)

    context = {
        'form': form
    }

    return render(request, "storagemanager/newobject.html", context)


def deleteobject(request, object_id):
    try:
        object = get_object_or_404(Object, pk=object_id)
    except Object.DoesNotExist:
        raise Http404("Object does not exist")
    object.delete()

    latest_objects_list = Object.objects.order_by("create_date")[:1000000]
    context = {"latest_objects_list": latest_objects_list}

    return render(request, "storagemanager/objects.html", context)