from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from project.models import *
import json


@require_http_methods(['GET', 'OPTIONS'])
def list_statistics(request):
    if request.method == 'GET':
        daily = []
        weekly = []
        monthly = []
        daily_statistics = DailyStatistics.objects.values()
        weekly_statistics = WeeklyStatistics.objects.values()
        monthly_statistics = MonthlyStatistics.objects.values()
        for i in daily_statistics:
            daily.append({
                'daily_lowest_price': i['daily_lowest_price'],
                'daily_maximum_price': i['daily_maximum_price'],
                'daily_total_price': i['daily_total_price'],
                'daily_average_price': i['daily_average_price']
            })

        for i in monthly_statistics:
            monthly.append({
                'monthly_lowest_price': i['monthly_lowest_price'],
                'monthly_maximum_price': i['monthly_maximum_price'],
                'monthly_total_price': i['monthly_total_price'],
                'monthly_average_price': i['monthly_average_price']
            })

        for i in weekly_statistics:
            weekly.append({
                'weekly_lowest_price': i['weekly_lowest_price'],
                'weekly_maximum_price': i['weekly_maximum_price'],
                'weekly_total_price': i['weekly_total_price'],
                'weekly_average_price': i['weekly_average_price']
            })

        return HttpResponse(json.dumps({'daily': daily, 'weekly': weekly, 'monthly': monthly}))
