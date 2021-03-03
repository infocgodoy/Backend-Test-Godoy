from django.shortcuts import render
from django.http import HttpResponse
from gestionClientes.models import Clientes, Pedidos
from django.utils import timezone

# Create your views here.

def login(request):

    return render(request, "login_t.html")

def login_res(request):

    if request.GET["rut"]:

        #mensaje="Rut a buscar: %r" %request.GET["rut"]
        rut=request.GET["rut"]
        
        cliente=Clientes.objects.filter(rut=rut).first()

        
        
        if cliente.group == 'Admin':

            return render(request, "login_admin.html", {"cliente":cliente, "query":rut})

        else:
            
            now=timezone.now()
            hoy=now.day

            if now.hour < 11:

                cliente_id=cliente.id
                pedido=Pedidos.objects.filter(id_cliente=cliente_id,fecha__lte=now).order_by('fecha').last()
                
                if pedido.fecha.day == hoy:

                    return render(request, "login_cliente.html", {"cliente":cliente, "pedido":'temprano', "hoy":now, "ultimo":pedido, "comio":1})

                else:

                    return render(request, "login_cliente.html", {"cliente":cliente, "pedido":'temprano', "hoy":now, "ultimo":pedido, "comio":0})

            else:
                                    
                return render(request, "login_cliente.html", {"cliente":cliente, "pedido":'tarde', "hora":now.hour, "min":now.minute})  

    else:

        mensaje="No has ingresado nada"

    return HttpResponse(mensaje)