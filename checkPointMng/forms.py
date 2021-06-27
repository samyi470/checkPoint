from django import forms
from django.forms import ModelForm

# LAX terminal search attempt
from .models import LAXDay


# class to hold calendar selection
# class DateInput(forms.DateInput):
#     input_type = 'date'


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
            # 'primary': DateInput(),
            'start': forms.DateInput(attrs={'class': 'datepicker'}),
            'end': forms.DateInput(attrs={'class': 'datepicker'}),
        }
