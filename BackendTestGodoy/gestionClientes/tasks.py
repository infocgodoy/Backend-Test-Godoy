from celery import shared_task
from django.http import HttpResponse
#from django_celery import settings


#from gestionClientes.tasks import *
#celery -A BackendTestGodoy worker -l INFO
@shared_task
def envia_menu_diario():

    return HttpResponse('estamos trabajando para usted')