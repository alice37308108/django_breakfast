from django.db import models


class Breakfast(models.Model):
    date = models.DateField()
    hours_of_sleep = models.IntegerField()
    breakfast = models.CharField(max_length=200)
    sleep_quality = models.IntegerField()
    feeling = models.IntegerField()
    sweet = models.CharField(max_length=200, null=True, blank=True)
    memo = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.date.strftime('%Y/%m/%d')
