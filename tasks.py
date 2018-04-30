from celery import app
import time

@app.task
def addition(s,w):
    time.sleep(20)
    return s+w

@app.task
def get_no_char(string):
    return len(string)

@app.task
def reverser(string):
    return string[::-1]
