from __future__ import absolute_import, unicode_literals
from celery_master import app
import time

@app.task
def get_no_char(string):
    time.sleep(50)
    return len(string)

@app.task
def reverser(string):
    time.sleep(50)
    return string[::-1]
