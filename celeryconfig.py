# specify whihc messaging brocker to be used
broker_url = 'amqp://localhost//'
# can specify the tasks that celery can to trigger
imports = ('celery_learn.tasks', )
# backend for celery
result_backend = 'db+postgresql://postgres:useruser@localhost/celery_test_base'
