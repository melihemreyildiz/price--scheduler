from django.db import models
# Create your models here.


class Infos(models.Model):
    daily_lowest_price = models.FloatField(default=0)
    daily_maximum_price = models.FloatField(default=0)
    daily_average_price = models.FloatField(default=0)
    daily_total_price = models.FloatField(default=0)
    date = models.DateTimeField(verbose_name='Operation Date Time', auto_now_add=True)


class DailyStatistics(models.Model):
    daily_lowest_price = models.FloatField(default=0)
    daily_maximum_price = models.FloatField(default=0)
    daily_average_price = models.FloatField(default=0)
    daily_total_price = models.FloatField(default=0)
    date = models.DateTimeField(verbose_name='Operation Date Time', auto_now_add=True)


class WeeklyStatistics(models.Model):
    weekly_lowest_price = models.FloatField(default=0)
    weekly_maximum_price = models.FloatField(default=0)
    weekly_average_price = models.FloatField(default=0)
    weekly_total_price = models.FloatField(default=0)
    date = models.DateTimeField(verbose_name='Operation Date Time', auto_now_add=True)


class MonthlyStatistics(models.Model):
    monthly_lowest_price = models.FloatField(default=0)
    monthly_maximum_price = models.FloatField(default=0)
    monthly_average_price = models.FloatField(default=0)
    monthly_total_price = models.FloatField(default=0)
    date = models.DateTimeField(verbose_name='Operation Date Time', auto_now_add=True)
