from datetime import datetime, timedelta

from django_celery_beat.models import IntervalSchedule, PeriodicTask


def create_habit_schedule(habit):
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=10,
        period=IntervalSchedule.SECONDS,
    )

    PeriodicTask.objects.create(
        interval=schedule,
        name='Send habit message',
        task='habit_tracker.tasks.habit_task',
        expires=datetime.now() + timedelta(seconds=30)
    )