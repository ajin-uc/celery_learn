from __future__ import absolute_import, unicode_literals
from celery_master import app

@app.task
def get_no_char(string):
    return len(string)

@app.task
def reverser(string):
    return string[::-1]
