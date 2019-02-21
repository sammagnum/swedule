
#from django.forms import forms as Forms
from django import forms

from timezone_field import TimeZoneFormField

import pytz


class TZForm(forms.Form):
    IBM_TZS = [
        'US/Alaska',
        'US/Arizona',
        'US/Central',
        'US/Eastern',
        'US/Hawaii',
        'US/Mountain',
        'US/Pacific',
        'Asia/Manila',
    ]

    timezone = TimeZoneFormField(choices=[(tz, tz) for tz in IBM_TZS],
                                 widget=forms.Select(attrs={'onchange': 'form.submit();'}))










