from django.utils import timezone


SUNDAY = 6


def get_date_range(date):
    dates_monday = date - timezone.timedelta(days=date.weekday())
    dates_sunday = dates_monday + timezone.timedelta(days=SUNDAY)
    return [dates_monday, dates_sunday]


def get_na_start_of_day(t_zone):
    h = {
        'US/Alaska': 4,
        'US/Arizona': 6,
        'US/Central': 7,
        'US/Eastern': 8,
        'US/Hawaii': 3,
        'US/Mountain': 6,
        'US/Pacific': 5,
        'Asia/Manila': 21,
    }
    return h[t_zone]


def _next(current):
    date = current + timezone.timedelta(weeks=1)
    return date


def _prev(current):
    date = current - timezone.timedelta(weeks=1)
    return date


def set_timezone(request, new_timezone):
    request.session['django_timezone'] = new_timezone

def get_timezone(request):
    return request.session['django_timezone']