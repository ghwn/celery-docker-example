"""
https://docs.celeryq.dev/en/stable/userguide/configuration.html
"""

broker_url = "amqp://rabbit:rabbit@rabbitmq:5672/"

result_backend = "redis://redis:6379/0"
result_extended = True
result_expires = 3600

enable_utc = True
timezone = "Asia/Seoul"
