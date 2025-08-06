from celery import Celery

app = Celery("app", broker="amqp://rabbit:rabbit@rabbitmq:5672/", include=["app.tasks"])
