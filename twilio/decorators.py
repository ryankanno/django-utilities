from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.conf import settings
from django.http import HttpResponseBadRequest

from functools import wraps

from twilio.util import RequestValidator


TWILIO_AUTH_TOKEN  = getattr(settings, 'TWILIO_AUTH_TOKEN', None)


def twilio(fxn):
    """
    Decorator for twilio callback function
    """
    @csrf_exempt
    @require_POST
    def wrapper(request, *args, **kwargs):
        url       = request.build_absolute_uri()
        signature = request.META.get('HTTP_X_TWILIO_SIGNATURE', '')
        validator = RequestValidator(TWILIO_AUTH_TOKEN)

        if v.validate(url, request.POST, sig):
            return fxn(request, *args, **kwargs)
        else:
            return HttpResponseBadRequest('Unable to validate Twilio signature')
    return wraps(fxn)(wrapper)
