from django.urls import path, include, register_converter

from s_app import converters
from . import views

register_converter(converters.DateConverter, 'dd-mm-yyyy')
urlpatterns = [
    path('', views.index, name='index'),
    path('swe/<str:username>/', views.swe, name='swe'),
    path('swe/<str:username>/<dd-mm-yyyy:date>/', views.swe, name='next_week'),
    path('swe/<str:username>/<dd-mm-yyyy:date>/', views.swe, name='prev_week'),
    path('userhome/', views.userhome, name='userhome'),
    path('teamlead/', views.teamlead, name='teamlead_url'),
    path('team/<slug:team_slug>/',views.team, name='team'),


    # Add Django site authentication urls (for login, logout, password management)
    path('accounts/', include('django.contrib.auth.urls')),
]
