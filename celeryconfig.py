broker_url = 'amqp://localhost//'
imports = ('tasks',)
task_routes = {
    'tasks.get_no_char':{'queue':'count-queue'},
    'tasks.reverser': {'queue': 'reverse-queue'}
}
