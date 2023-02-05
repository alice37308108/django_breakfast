from django import forms


class BreakfastForm(forms.Form):
    date = forms.DateField()
    hours_of_sleep = forms.IntegerField()
    breakfast = forms.CharField(max_length=200)
    sleep_quality = forms.IntegerField()
    feeling = forms.IntegerField()
    sweet = forms.CharField(max_length=200, required=False)
    memo = forms.CharField(max_length=200, required=False)