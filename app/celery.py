from celery import Celery

app = Celery("app", include=["app.tasks"])
app.config_from_object("app.celeryconfig")
