
broker_url = 'amqp://localhost//'

result_backend = 'db+postgresql://postgres:useruser@localhost/celery_test_base'

imports = ('celery_learn.tasks', )
