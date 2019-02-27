import pytz

from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin
from s_app.models import Swe
from s_app.util import set_timezone
from django.contrib.auth.models import User


class TimezoneMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            tzname = Swe.objects.get(user__exact=request.user).timezone
        else:
            tzname = None
        print(str(tzname) + " this is tz name")

        print(tzname)
        if tzname:
            set_timezone(request, str(tzname))
            timezone.activate(tzname)
        else:
            set_timezone(request, '')
            timezone.deactivate()