from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.shortcuts import resolve_url
from django.urls import reverse


class Breakfast(models.Model):
    date = models.DateField(verbose_name='日付', unique=True)
    hours_of_sleep = models.IntegerField(verbose_name='睡眠時間', )
    breakfast = models.CharField(max_length=30, verbose_name='朝ごはん')
    sleep_quality = models.IntegerField(verbose_name='睡眠の質')
    feeling = models.IntegerField(verbose_name='今日の気分', validators=[MinValueValidator(1), MaxValueValidator(5)])
    sweet = models.CharField(max_length=200, blank=True, verbose_name='おやつ')
    memo = models.CharField(max_length=200, blank=True, verbose_name='メモ')  # CharField、TextFieldときはnull=Trueはいらない
    tags = models.ManyToManyField('Tag', blank=True, verbose_name='タグ')

    def __str__(self):
        return self.date.strftime('%Y/%m/%d')

    def get_feeling_stars(self):  # オブジェクトのメソッドとして呼び出せる、contentに書くとわすれるので、モデルのメソッドにしてそれを呼び出す
        return '★' * self.feeling + '☆' * (5 - self.feeling)

    def get_absolute_url(self):
        return resolve_url('breakfast:detail', pk=self.pk)  # 戻り値はbreakfastのdetail
        # return reverse('breakfast:detail', kwargs={'pk': self.pk})


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True, )
    slug = models.SlugField(max_length=20, unique=True, )

    def __str__(self):
        return f'{self.id}: {self.name}'
