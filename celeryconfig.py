from kombu import Queue, Exchange, binding
from router import tasks_router

broker_url = 'amqp://localhost//'

imports = ('tasks',)

result_backend = 'db+postgresql://postgres:useruser@localhost/celery_test_base'

task_default_queue = 'default'

task_queues = (
    Queue('addition-queue', routing_key='addition-queue'),
    Queue('periodic-queue', routing_key='periodic-queue'),
    Queue('testing-queue', routing_key='testing-queue'),
    Queue('count-queue', routing_key='count-queue'),
    Queue('reverse-queue', routing_key='reverse-queue'),
)

task_default_exchange = 'tasks'
task_default_exchange_type = 'direct'
task_default_routing_key = 'tasks.default'

beat_schedule = {
    'every-5-sec': {
        'task':'tasks.add',
        'schedule': 3.0,
        'args':(1,4)
    },
}

task_routes = [
    tasks_router,
    {
        'tasks.get_no_char':{'queue':'count-queue'},
        'tasks.reverser': {'queue': 'reverse-queue'}
    },
]
