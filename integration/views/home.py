from django.shortcuts import render, redirect
from django.urls import reverse
import jdatetime
from integration.helpers.jalali_datetime_helper import month_name, weekday_name
# from jdatetime import tzinfo
import datetime


class Home:
    @staticmethod
    def index(request):
        if request.user.is_authenticated:
            jdatetime.set_locale('fa_IR')
            # print(jdatetime.datetime.now().hour)
            # print(jdatetime.datetime.now().minute)
            # print(datetime.datetime.now().hour)
            # print(datetime.datetime.now().minute)
            return render(request, 'integration/index.html', {
                'user': {'name': 'user1'},
                'local_time_hour': datetime.datetime.now().hour,
                'local_time_minute': datetime.datetime.now().minute,

                'local_date_year': jdatetime.datetime.now().year,
                'local_date_month': month_name(jdatetime.datetime.now().month),
                'local_date_day': jdatetime.datetime.now().day,
                'local_date_weekday': weekday_name(jdatetime.datetime.now().weekday()),
            })
        else:
            return redirect(reverse("user.login"))
