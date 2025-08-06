# Celery Docker Example

This project uses:
- **RabbitMQ** as broker
- **Redis** as backend
- **Celery Beat** as scheduler
- **Flower** as monitoring tool

## Run Server

```shell
$ docker compose up --build
```

## RabbitMQ Monitoring

http://localhost:15672 (Username: rabbit, Password: rabbit)

## Flower Monitoring

http://localhost:5555
