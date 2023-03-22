from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse


class Breakfast(models.Model):
    date = models.DateField(verbose_name='日付', unique=True)
    hours_of_sleep = models.IntegerField(verbose_name='睡眠時間')
    breakfast = models.CharField(max_length=5, verbose_name='朝ごはん')
    sleep_quality = models.IntegerField(verbose_name='睡眠の質')
    feeling = models.IntegerField(verbose_name='今日の気分', validators=[MinValueValidator(1), MaxValueValidator(5)])
    sweet = models.CharField(max_length=200, blank=True, verbose_name='おやつ')
    memo = models.CharField(max_length=200, blank=True, verbose_name='メモ')  # CharField、TextFieldときはnull=Trueはいらない


    def __str__(self):
        return self.date.strftime('%Y/%m/%d')

    def get_absolute_url(self):
        return reverse('breakfast:detail', kwargs={'pk': self.pk})
