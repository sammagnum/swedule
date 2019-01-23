from django.contrib import admin
from s_app.models import Request, Teamlead, Team, Manager, Swe, Event

# Register your models here.

admin.site.register(Request)
admin.site.register(Teamlead)
admin.site.register(Team)
admin.site.register(Manager)
admin.site.register(Swe)
admin.site.register(Event)

