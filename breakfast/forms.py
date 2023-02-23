from django import forms
from django.core.exceptions import ValidationError
from django.forms import Textarea
from django.utils import timezone

from .models import Breakfast


class BreakfastModelForm(forms.ModelForm):
    class Meta:
        model = Breakfast
        fields = "__all__"


class BreakfastForm(forms.Form):
    date = forms.DateTimeField(label='日付')
    hours_of_sleep = forms.IntegerField(label='睡眠時間')
    breakfast = forms.CharField(label='朝食')
    sleep_quality = forms.IntegerField(label='睡眠の質')
    feeling = forms.IntegerField(label='気分')
    sweet = forms.CharField(label='お菓子')
    memo = forms.CharField(label='メモ')

    def clean_date(self):
        date = self.cleaned_data['date']
        if date > timezone.now():
            raise ValidationError('未来の日付は入力できません。')
        return date

    def clean_hours_of_sleep(self):
        hours_of_sleep = self.cleaned_data['hours_of_sleep']
        if hours_of_sleep < 0:
            raise ValidationError('0以上の値を入力してください。')
        elif hours_of_sleep > 24:
            raise ValidationError('24以下の値を入力してください。')
        return hours_of_sleep

    def clean_sleep_quality(self):
        sleep_quality = self.cleaned_data['sleep_quality']
        if sleep_quality < 0:
            raise ValidationError('0以上の値を入力してください。')
        elif sleep_quality > 5:
            raise ValidationError('5以下の値を入力してください。')
        return sleep_quality
