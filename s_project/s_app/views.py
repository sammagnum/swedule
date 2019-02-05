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
from s_app.util import get_date_range
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



def swe(request, username):


    user = User.objects.get(username=username)
    swe = Swe.objects.get(user__username=username)
    tz = swe.timezone
    timezone.activate(tz)
    work_week = get_date_range(timezone.now())
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

            messages.success(request,'Your Timezone has been updated')
            return HttpResponseRedirect(username)
    else:
        form = TZForm()
    context = {
        'user_url': username,
        'tmz': swe.timezone,
        'form': form,
        'first_name':    user.first_name,
        'monday': '{:%m/%d/%Y}'.format(work_week[0]),
        'sunday': '{:%m/%d/%Y}'.format(work_week[1]),
        'schedule': Event.objects.filter(swe__user_id=user.id, start_time__gte=work_week[0],
                                         start_time__lte=work_week[1])
    }
    return render(request, 'swe.html', context=context)


#def swe(request):
    #return render(request, 'swe.html')

