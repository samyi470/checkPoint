from django import forms
from django.forms import ModelForm

# terminal search
from .models import LAXDay


class DateInput(forms.DateInput):
    input_type = 'date'


YEARS = [
    ("2020", "2020"),
    ("2019", "2019"),
    ("2018", "2018"),
    ("2017", "2017"),
    ("2016", "2016"),
    ("2015", "2015"),
]


class LAXDayForm(ModelForm):
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
            # 'twentyTwenty',
            # 'twentyNineteen',
            # 'twentyEighteen',
            # 'twentySeventeen',
            # 'twentySixteen',
            # 'twentyFifteen',
            'compare',
        ]
        widgets = {
            'primary': DateInput(),
        }
