from celery import shared_task
from telebot import TeleBot
from datetime import datetime, timedelta
from config import settings
from config.celery import app
from habit_tracker.models import Habit


@shared_task
def send_message_habit():
    bot = TeleBot(settings.TG_BOT_API)
    time_now = datetime.now()
    start_time = time_now - timedelta(minutes=1)
    habit = Habit.objects.filter(time__gte=start_time)

    for habit in habit.filter(time__lte=time_now):
        message = f"Не забудьте в {habit.place} {habit.action} в {habit.time}"
        bot.send_message(message, 'habit.user.chat_id')
