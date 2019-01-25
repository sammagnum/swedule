from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('swe/<str:username>', views.swe, name='swe'),
]
