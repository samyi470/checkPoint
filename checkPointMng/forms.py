from django import forms
from django.forms import ModelForm

# LAX terminal search attempt
from .models import LAXDay
from .models import LAXMonth
from .models import LAXYear


# class to hold calendar selection
class DateInput(forms.DateInput):
    input_type = 'date'


# choices for MultipleChoiceField
YEARS = [
    ("2020", "2020"),
    ("2019", "2019"),
    ("2018", "2018"),
    ("2017", "2017"),
    ("2016", "2016"),
    ("2015", "2015"),
]


class LAXDayForm(ModelForm):
    # to check multiple years to compare
    compare = forms.MultipleChoiceField(
        required=False,
        label='Compare',
        widget=forms.CheckboxSelectMultiple,
        choices=YEARS,
    )

    class Meta:
        model = LAXDay
        fields = [
            'terminal',
            'primary',
            'compare',
        ]

        # to select a date from calendar
        widgets = {
            'primary': DateInput(),
        }


class LAXMonthForm(ModelForm):
    # to check multiple years to compare
    compare = forms.MultipleChoiceField(
        required=False,
        label='Compare',
        widget=forms.CheckboxSelectMultiple,
        choices=YEARS,
    )

    class Meta:
        model = LAXMonth
        fields = [
            'terminal',
            'primaryYear',
            'primaryMonth',
        ]


class LAXYearForm(ModelForm):
    # to check multiple years to compare
    compare = forms.MultipleChoiceField(
        required=False,
        label='Compare',
        widget=forms.CheckboxSelectMultiple,
        choices=YEARS,
    )

    class Meta:
        model = LAXYear
        fields = [
            'terminal',
            'primaryYear',
        ]