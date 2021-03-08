from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django_celery import settings


#from gestionClientes.tasks import *
#celery -A BackendTestGodoy worker -l INFO
@shared_task
def envia_menu_diario():
    asunto = 'Mensaje de prueba'
    mensaje = 'Bienvenido, esto es un mensaje de prueba CELERY, RABBITMQ y DJANGO'
    user = User.objets.all()

    for x in users:
        send_mail(asunto, mensaje,)