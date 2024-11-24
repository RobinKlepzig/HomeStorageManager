from django.conf import settings


def hostnameandport(request):
    return {'HOSTNAMEANDPORT': settings.HOSTNAMEANDPORT}
