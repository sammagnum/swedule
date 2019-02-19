from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.urls import reverse
from timezone_field import TimeZoneFormField, forms
import pytz
from .models import Team, Event, Swe
from django.contrib.auth.models import User
import datetime
from s_app.util import get_date_range, get_na_start_of_day, _next
from s_app.forms import TZForm
from django.utils import timezone

# Create your views here.


@login_required
def userhome(request):
    return HttpResponseRedirect(
               reverse(swe, args=[request.user.username]))


def index(request):
    """View function for home page of site."""



    team_cnt = str(Team.objects.all().count())

    context = {
        'team_cnt': team_cnt,

    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


def swe(request, username, date=None):

    user = User.objects.get(username=username)
    swe = Swe.objects.get(user__username=username)
    tz = swe.timezone
    timezone.activate(tz)
    if date is not None:
        current = timezone.make_aware(datetime.datetime.combine(date, datetime.datetime.min.time()), tz, True)
        current = current.replace(tzinfo=timezone.utc)
    if date is None:
        current = timezone.now()
        current = current.replace(hour=0, minute=0, second=0, microsecond=0)

    work_week = get_date_range(current)
    if user.id != Swe.objects.get(user__username=username).user.id:
        return HttpResponseNotFound('SWE not found:' + str(user.id) )
    # if this is a POST request we need to process the form data
    if request.method == 'POST':


        # create a form instance and populate it with data from the request:
        form = TZForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.clean()
            swe.timezone = form.cleaned_data["timezone"]
            swe.save()
            print(request.get_full_path())
            messages.success(request,'Your Timezone has been updated')
            return HttpResponseRedirect(request.get_full_path())
        else:
            print(form.errors)
    else:
        form = TZForm()
    morning = get_na_start_of_day(str(tz))
    days_of_week=[
        "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"
    ]

    next_week = _next(current)


    context = {
        'user_url': username,
        'tmz': swe.timezone,
        'form': form,
        'first_name':    user.first_name,
        'next_weeks_date': str(next_week).split(" ")[0],
        'monday': '{:%m/%d/%Y}'.format(work_week[0]),
        'sunday': '{:%m/%d/%Y}'.format(work_week[1]),
        'schedule': Event.objects.filter(swe__user_id=user.id, start_time__gte=work_week[0],
                                         start_time__lte=work_week[1]),
        'range_i': range(morning,morning+13),
        'dow': days_of_week

    }
    timezone.deactivate()
    return render(request, 'swe.html', context=context)


#def swe(request):
    #return render(request, 'swe.html')

