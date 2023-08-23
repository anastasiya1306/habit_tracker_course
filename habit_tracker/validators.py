from datetime import datetime

from rest_framework import serializers


class HabitValidator:
    def __call__(self, value):
        if value.get('related_habit') and value.get('reward'):
            raise serializers.ValidationError('Нельзя одновременно указывать связанную привычку и вознаграждение')
        if value.get('execution_time') > datetime.time(hour=0, minute=2, second=0):
            raise serializers.ValidationError('Время выполнения должно быть не больше 120 секунд')
        if value.get('related_habit') and not value.get('related_habit').is_pleasant:
            raise serializers.ValidationError(
                'В связанные привычки могут попадать только привычки с признаком приятной привычки')
        if value.get('frequency') > 7:
            raise serializers.ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')
