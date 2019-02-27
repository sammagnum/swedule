from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.utils import timezone

from s_app.forms import TZForm
from s_app.models import Swe,Event,Teamlead

import pytz
import datetime

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


def _next_w(current):
    date = current + timezone.timedelta(weeks=1)
    return date


def _prev_w(current):
    date = current - timezone.timedelta(weeks=1)
    return date

def _next_d(current):
    date = current + timezone.timedelta(weeks=1)
    return date


def _prev_d(current):
    date = current - timezone.timedelta(weeks=1)
    return date

def set_timezone(request, new_timezone):
    request.session['django_timezone'] = new_timezone


def get_timezone(request):
    return request.session['django_timezone']


def configure_timezone_aware(date, tz):
    if date is not None:
        current = timezone.make_aware(datetime.datetime.combine(date, datetime.datetime.min.time()), pytz.timezone(tz), True)
        current = current.replace(tzinfo=timezone.utc)
    if date is None:
        current = timezone.now()
        current = current.replace(hour=0, minute=0, second=0, microsecond=0)
    return current


def get_swe(request,username,date = None):
    context = get_shared_calendar_context(request, date)
    work_week = context['work_week']
    user = User.objects.get(username=username)
    swe = Swe.objects.get(user__username=username)
    if user.id != Swe.objects.get(user__username=username).user.id:
        return HttpResponseNotFound('SWE not found:' + str(user.id))
    context['user_url'] = username
    context['swe'] = swe
    context['first_name'] = user.first_name
    context['schedule'] = Event.objects.filter(swe__user_id=user.id, start_time__gte=work_week[0],start_time__lte=work_week[1])
    context['is_teamlead'] = Teamlead.objects.filter(user__exact=request.user.id).exists()
    return context


def get_shared_calendar_context(request,date):
    tz = get_timezone(request)
    current = configure_timezone_aware(date, tz)
    work_week = get_date_range(current)
    morning = get_na_start_of_day(str(tz))
    days_of_week = [
        "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"
    ]
    context = {
        'today': '{:%A %d}'.format(current),
        'next_weeks_date': str(_next_w(current)).split(" ")[0],
        'prev_weeks_date': str(_prev_w(current)).split(" ")[0],
        'work_week': work_week,
        'monday': '{:%m/%d/%Y}'.format(work_week[0]),
        'sunday': '{:%m/%d/%Y}'.format(work_week[1]),
        'range_i': range(morning, morning + 13),
        'dow': days_of_week
    }
    return context


def swe_post(request,swe):
    # create a form instance and populate it with data from the request:
    form = TZForm(request.POST)
    # form = TZForm(resque)
    # check whether it's valid:
    if form.is_valid():
        form.clean()
        swe.timezone = form.cleaned_data["timezone"]
        set_timezone(request, str(swe.timezone))
        swe.save()
        messages.success(request, 'Your Timezone has been updated')
        return request
    else:
        print(form.errors)
    return request


def swe_not_post(request):
    return TZForm(initial={'timezone': str(get_timezone(request))})
