from celery import Celery

app = Celery(
    "app",
    broker="amqp://rabbit:rabbit@rabbitmq:5672/",
    backend="redis://redis:6379/0",
    include=["app.tasks"],
)
