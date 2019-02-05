from django.utils import timezone
import pytz

SUNDAY = 6

def get_date_range(date):
    dates_monday = date - timezone.timedelta(days=date.weekday())
    dates_sunday = dates_monday + timezone.timedelta(days=SUNDAY)
    return [dates_monday,dates_sunday]

