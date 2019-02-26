from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, HttpRequest, HttpResponseForbidden
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.urls import reverse
from timezone_field import TimeZoneFormField, forms
import pytz
from .models import Team, Event, Swe, Teamlead
from django.contrib.auth.models import User
import datetime
from s_app.util import get_date_range, get_na_start_of_day, _next, _prev, set_timezone, get_swe, swe_post, swe_not_post
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


@login_required
def team(request,team_slug):
    team_members = Swe.objects.filter(team__slug=team_slug)
    for member in team_members:
        member_context = get_swe()
    return HttpResponse(team_members)


@login_required
def teamlead(request):
    this_user = request.user.id
    if Teamlead.objects.filter(user__exact=this_user):  # team view for teamleads

        team_this_user_leads = Team.objects.filter(lead__exact=this_user)
        team_slug=team_this_user_leads[0].slug
        old_path = request.get_full_path()
        new_path = old_path.replace("lead/", "/" + str(team_slug))

        return HttpResponseRedirect(new_path)
    else:  # not a teamlead
        return HttpResponseForbidden("You made a wrong turn, you do not have access to this page.")


@login_required
def swe(request, username, date=None):
    context = get_swe(request,username,date)
    if request.method == 'POST':
        return HttpResponseRedirect(swe_post(request, context['swe']).get_full_path())
    else:
        context['form'] = swe_not_post(context['tmz'])

    return render(request, 'swe.html', context=context)


