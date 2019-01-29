from django.http import HttpResponseNotFound
from django.shortcuts import render

from .models import Team, Event, Swe
from django.contrib.auth.models import User
import datetime
from s_app.util import get_date_range_m_f

# Create your views here.


def index(request):
    """View function for home page of site."""

    team_cnt = str(Team.objects.all().count())

    context = {
        'team_cnt': team_cnt,

    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


def swe(request, username):
    work_week = get_date_range_m_f(datetime.date.today())
    user = User.objects.get(username=username)
    sam = Swe.objects.get(user__username=username)
    if user.id != Swe.objects.get(user__username=username).user.id:
        return HttpResponseNotFound('SWE not found:' + str(user.id) + " " + str(sam.user.id))
    context = {
        'first_name':    user.first_name,
        'monday': work_week[0],
        'friday': work_week[1],
        'schedule': Event.objects.filter(user, start_time__gte=work_week[0],
                                         start_time__lte=work_week[2])
    }
    return render(request, 'swe.html', context=context)


#def swe(request):
    #return render(request, 'swe.html')

