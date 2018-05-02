from celery import Celery

# since it is the local we give localhost for the broker
# if a remote host is to be used then specify
# the IP of the host
app =  Celery()
app.config_from_object('celeryconfig')
