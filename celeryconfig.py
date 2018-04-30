from kombu import Exchange, Queue

broker_url = 'amqp://localhost//'

imports = ('celery_learn.tasks',)
