def tasks_router(name, args, kwargs, options=None, task=None, **kw):
    if name == 'tasks.add':
        return 'addition-queue'

    if name == 'tasks.periodic_task_test':
        return 'periodic-queue'

    if name == 'tasks.test_task':
        return 'testing-queue'
