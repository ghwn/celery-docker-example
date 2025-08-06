"""
https://docs.celeryq.dev/en/stable/userguide/configuration.html
"""

from celery.schedules import crontab

broker_url = "amqp://rabbit:rabbit@rabbitmq:5672/"

result_backend = "redis://redis:6379/0"
result_extended = True
result_expires = 3600
result_persistent = True

enable_utc = True
timezone = "Asia/Seoul"

beat_schedule = {
    "task-a": {
        "task": "app.tasks.add",
        "args": (10, 20),
        "schedule": crontab(minute="*/1"),  # every minute
    },
}
