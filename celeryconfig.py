from kombu import Queue, Exchange

broker_url = 'amqp://localhost//'
imports = ('tasks',)
task_queues = (
    Queue('addition-queue', Exchange('direct'), routing_key='addition-queue'),
)
task_default_queue = 'default-queue'
task_default_exchange_type = 'direct'
task_routes = [
    'router.tasks_router',
    {
        'tasks.get_no_char':{'queue':'count-queue'},
        'tasks.reverser': {'queue': 'reverse-queue'}
    },
]
