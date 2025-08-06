from celery import Celery

app = Celery("celery-docker-example", include=["app.celery.tasks"])
app.config_from_object("app.celery.celeryconfig")
