from celery import shared_task
from django.http import HttpResponse
from django.shortcuts import render
from BackendTestGodoy import settings
import requests
import sys
import getopt
#from django_celery import settings


#from gestionClientes.tasks import *
#celery -A BackendTestGodoy worker -l INFO
#esta api ya fue probada con exito en mi slack
@shared_task
def enviar_menu_celery():    
    payload = '{"text":"El menu de hoy es http://127.0.0.1:8000/solo_menu/9b1deb3d-3b7d-4bsd-9zdd-2b0d7b3dcb6d"}'
    response = requests.post('https://hooks.slack.com/services/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',
    data=payload)

    return True