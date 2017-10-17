from django import forms
import datetime


class DateRangeForm(forms.Form):
    start_date = forms.DateTimeField(initial=datetime.date.today)
    end_date = forms.DateTimeField(initial=datetime.date.today)

    #this is comment
