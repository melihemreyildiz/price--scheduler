import requests
from django.http import HttpResponse
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import register_events, register_job, DjangoJobStore
import json
import pytz
from datetime import datetime
from project.models import *
import datetime as DT
from django.db.models import Q

scheduler = BackgroundScheduler(timezone='UTC')
today = datetime.utcnow().replace(tzinfo=pytz.utc)


def common_props(datas):
    min_trascation = min(list(datas), key=lambda x: x['daily_lowest_price'])['daily_lowest_price']
    max_trascation = max(list(datas), key=lambda x: x['daily_maximum_price'])['daily_maximum_price']
    total_volume = sum(float(item['daily_total_price']) for item in list(datas))
    average = total_volume / len(datas)
    return min_trascation, max_trascation, total_volume, average


@register_job(scheduler, "interval", minutes=5)
def read_datas():
    r = requests.get('https://www.bitexen.com/api/v1/order_book/BTCTRY/')
    values = r.json()
    if values['status'] == 'success':
        min_trascation = min(values['data']['last_transactions'], key=lambda x: x['price'])['price']
        max_trascation = max(values['data']['last_transactions'], key=lambda x: x['price'])['price']
        # total_volume ==? total price
        total_volume = sum(float(item['price']) for item in values['data']['last_transactions'])
        average = total_volume / len(values['data']['last_transactions'])
        Infos.objects.create(
            daily_lowest_price = min_trascation,
            daily_maximum_price= max_trascation,
            daily_total_price=total_volume,
            daily_average_price=average,
        )
        return HttpResponse(json.dumps(values))


@register_job(scheduler, "interval", minutes=60*24)
def daily_check():
    datas = Infos.objects.filter(date__day=today.day).values()
    if datas:
        min_trascation, max_trascation, total_volume, average = common_props(datas)
        DailyStatistics.objects.create(
            daily_lowest_price=min_trascation,
            daily_maximum_price=max_trascation,
            daily_total_price=total_volume,
            daily_average_price=average,
        )


@register_job(scheduler, "interval", minutes=60*24*7)
def weekly_check():
    datas = Infos.objects.filter(Q(date__gte=today - DT.timedelta(days=7)) & Q(date__lte=today)).values()
    if datas:
        min_trascation, max_trascation, total_volume, average = common_props(datas)
        WeeklyStatistics.objects.create(
            weekly_lowest_price=min_trascation,
            weekly_maximum_price=max_trascation,
            weekly_total_price=total_volume,
            weekly_average_price= average
        )


@register_job(scheduler, "interval", minutes=60*24*30)
def monthly_check():
    datas = Infos.objects.filter(Q(date__gte=today - DT.timedelta(days=30)) & Q(date__lte=today)).values()
    if datas:
        min_trascation, max_trascation, total_volume, average = common_props(datas)
        MonthlyStatistics.objects.create(
            monthly_lowest_price=min_trascation,
            monthly_maximum_price=max_trascation,
            monthly_total_price=total_volume,
            monthly_average_price=average,
        )
    else:
        return


def start():
    try:
        scheduler.add_jobstore(DjangoJobStore(), "default")
        register_events(scheduler)
        scheduler.start()
        print("Scheduler started!")
    except Exception as e:
        print(e)




