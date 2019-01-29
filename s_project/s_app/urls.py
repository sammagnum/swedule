from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('swe/<str:username>', views.swe, name='swe'),
    path('userhome/', views.userhome, name='userhome')
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
