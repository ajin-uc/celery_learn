def tasks_router(self, name, args, kwargs, options=None, task=None, **kw):
    if name == 'tasks.add':
        return 'adition-queue'
