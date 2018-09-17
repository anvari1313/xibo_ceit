from django.http import JsonResponse
from django.views import View
from integration.models import ClassroomSchedule
from xibo.requests import XiboRest
import integration.globs
import jdatetime
import datetime


class MinuteTicker(View):
    def get(self, request, *args, **kwargs):
        _now = str(jdatetime.datetime.now())
        dow = jdatetime.datetime.now().weekday()
        print(dow)
        now = datetime.datetime.now()
        # schedule_lists = TaskSchedule.objects.filter(
        #     task_datetime_hour=now.hour,
        #     task_datetime_min=now.minute,
        #     task_week_day=dow
        # )
        # for schedule in schedule_lists:
        #     XiboRest.update_widget(widget_id=schedule.widget.widget_id, text=schedule.text)

        classroom_schedules = ClassroomSchedule.objects.filter(
            start_time_hour=now.hour,
            start_time_min=now.minute,
            week_day=dow)

        for o in classroom_schedules:
            print(o)

        # s.week_day == dow and
        print('----------------------------------')
        for s in ClassroomSchedule.objects.all():
            print(s.start_time_hour, now.hour)
            print(s.start_time_min , now.minute)
            if s.start_time_hour == now.hour and s.start_time_min == now.minute:
                print(s)


        updated_widgets = []

        for classroom_schedule in classroom_schedules:
            print(classroom_schedule)
            teacher_widget_id = classroom_schedule.classroom.teacher_name_widget.widget_id
            teacher_name = classroom_schedule.teacher_name
            subject_widget_id = classroom_schedule.classroom.subject_name_widget.widget_id
            subject_name = classroom_schedule.subject_name
            # text_content = '<p style=\"text-align: right;\">' \
            #                '<span style=\"font-size: 48px;\">' \
            #                '{{teacher_name}}</span>' \
            #                '</p>\r\n\r\n<p style=\"text-align: right;\">&nbsp;</p>\r\n\r\n' \
            #                '<p style=\"text-align: right;\">' \
            #                '<span style=\"font-size: 48px;\">{{subject_name}}</span>' \
            #                '</p>\r\n'

            # text_content = '<p style=\"text-align: right;\">&nbsp;</p>\r\n\r\n<p style=\"text-align: right;\">&nbsp;</p>\r\n\r\n<p style=\"text-align: right;\"><span style=\"font-size:72px;\">{{subject_name}}</span></p>\r\n\r\n<p style=\"text-align: right;\">&nbsp;</p>\r\n\r\n<p style=\"text-align: right;\"><span style=\"font-size:72px;\">{{teacher_name}}</span></p>\r'
            text_content = integration.globs.class_content_temp
            formatted_context = text_content.replace('{{teacher_name}}', teacher_name).replace('{{subject_name}}',
                                                                                               subject_name)
            XiboRest.update_widget(
                widget_id=teacher_widget_id,
                text=formatted_context)
            XiboRest.update_widget(
                widget_id=subject_widget_id,
                text=formatted_context)

            updated_widgets.append({
                'TEACHER':{
                    'widget_id': teacher_widget_id,
                    'widget_text': teacher_name
                },
                'SUBJECT': {
                    'widget_id': subject_widget_id,
                    'widget_text': subject_name
                }})
            print('T: ' + str(classroom_schedule.classroom.teacher_name_widget.widget_id) +
                  ', ' + classroom_schedule.teacher_name)
            print('S: ' + str(classroom_schedule.classroom.subject_name_widget.widget_id) +
                  ', ' + classroom_schedule.subject_name)
            print()

        return JsonResponse({
            'NOW': _now,
            'DOW': dow,
            'UPDATED_WIDGETS': updated_widgets,
            # 'ALL': ClassroomSchedule.objects.all().
        })
