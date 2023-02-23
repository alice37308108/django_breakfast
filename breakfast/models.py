from django.db import models


class Breakfast(models.Model):
    date = models.DateField(verbose_name='日付')
    hours_of_sleep = models.IntegerField(verbose_name='睡眠時間')
    breakfast = models.CharField(max_length=200, verbose_name='朝ごはん')
    sleep_quality = models.IntegerField(verbose_name='睡眠の質')
    feeling = models.IntegerField(verbose_name='今日の気分')
    sweet = models.CharField(max_length=200, null=True, blank=True, verbose_name='おやつ')
    memo = models.CharField(max_length=200, null=True, blank=True, verbose_name='メモ')

    def __str__(self):
        return self.date.strftime('%Y/%m/%d')
