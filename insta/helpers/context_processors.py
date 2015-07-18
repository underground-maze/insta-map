from django.conf import settings


def django_settings(request):
    return {'SETTINGS': settings}
