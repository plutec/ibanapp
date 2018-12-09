# pylint: disable=unused-argument
from django.contrib.auth.models import User
from django.http import HttpResponse


def auth_allowed(backend, details, response, *args, **kwargs):
    email = details.get('email', None)
    print(email)
    user = User.objects.filter(email=email).exists()
    if not user:
        return HttpResponse(status=403)
    return None
