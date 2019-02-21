
from django.utils import timezone

class TimezoneMiddleware(object):
    def process_request(self,request):
        timezone.deactivate()
