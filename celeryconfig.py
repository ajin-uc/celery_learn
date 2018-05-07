from kombu import Queue, Exchange, binding

broker_url = 'amqp://localhost//'

imports = ('tasks',)

task_default_queue = 'default-queue'
task_default_exchange_type = 'direct'
task_default_routing_key = 'default-queue'

task_queues = (
    Queue('adition-queue', routing_key='adition-queue'),
    Queue('periodic-queue', routing_key='periodic-queue'),
    Queue('testing-queue', routing_key='testing-queue'),
    Queue('count-queue', routing_key='count-queue'),
    Queue('reverse-queue', routing_key='reverse-queue'),
)

task_create_missing_queues = False

task_routes = [
    'router.tasks_router',
    {
        'tasks.get_no_char':{'queue':'count-queue'},
        'tasks.reverser': {'queue': 'reverse-queue'}
    },
]
