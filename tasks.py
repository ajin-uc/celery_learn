from celery_utils import app
import time
import os
import django
import sys
from django.core.wsgi import get_wsgi_application

sys.path.append("/home/mis/work/attorney-bar/webapp/")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings')
django.setup()
get_wsgi_application()

from attorney_bar_app.models import CeleryTest

@app.task
def addition(s,w):
    time.sleep(20)
    return s+w

@app.task
def insertion(name, email):
    time.sleep(2)
    CeleryTest.objects.create(name=name, email=email)
    return "worked"

@app.task
def get_no_char(string):
    return len(string)

@app.task
def reverser(string):
    return string[::-1]
