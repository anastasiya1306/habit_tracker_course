from celery import shared_task
import telebot
from datetime import datetime, timedelta
from config import settings
from habit_tracker.models import Habit


@shared_task
def habit_task(habit):
    bot = telebot.TeleBot(settings.TELEGRAM_BOT_API)
    time_now = datetime.now()
    time_start_task = time_now - timedelta(minutes=1)
    habit_data = Habit.objects.filter(time__gte=time_start_task)

    for item in habit_data.filter(time__lte=time_now):
        message = f"В {item.place} не забудьте {item.action} в {item.time}"
        bot.send_message(message, 'item.user.chat_id')
