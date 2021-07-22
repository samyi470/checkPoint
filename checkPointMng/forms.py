from django import forms
from django.forms import ModelForm

from .models import LAXDay
from .models import LASDay
from .models import PHXDay


class LAXDayForm(ModelForm):
    class Meta:
        model = LAXDay
        fields = [
            'terminal',
            'start',
            'end',
        ]

        # to select a date from calendar
        widgets = {
            'start': forms.DateInput(attrs={'class': 'datepicker'}),
            'end': forms.DateInput(attrs={'class': 'datepicker'}),
        }


class LASDayForm(ModelForm):
    class Meta:
        model = LASDay
        fields = [
            'terminal',
            'start',
            'end',
        ]

        # to select a date from calendar
        widgets = {
            'start': forms.DateInput(attrs={'class': 'datepicker'}),
            'end': forms.DateInput(attrs={'class': 'datepicker'}),
        }


class PHXDayForm(ModelForm):
    class Meta:
        model = PHXDay
        fields = [
            'terminal',
            'start',
            'end',
        ]

        # to select a date from calendar
        widgets = {
            'start': forms.DateInput(attrs={'class': 'datepicker'}),
            'end': forms.DateInput(attrs={'class': 'datepicker'}),
        }

