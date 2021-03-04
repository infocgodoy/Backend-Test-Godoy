from django.shortcuts import render
from django.http import HttpResponse
from gestionClientes.models import Clientes, Pedidos, Platos, Menus
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
            cliente_id=cliente.id
            pedido=Pedidos.objects.filter(id_cliente=cliente_id,fecha__lte=now).order_by('fecha').last()
            
            if now.hour < 23:

                if pedido == None:

                    return render(request, "login_cliente.html", {"cliente":cliente, "tipo_pedido":'temprano', "hoy":now, "ultimo":pedido, "comio":0})
                                      
                elif pedido.fecha.day == hoy:

                    return render(request, "login_cliente.html", {"cliente":cliente, "tipo_pedido":'temprano', "hoy":now, "ultimo":pedido, "comio":1})

                else:

                    return render(request, "login_cliente.html", {"cliente":cliente, "tipo_pedido":'temprano', "hoy":now, "ultimo":pedido, "comio":0})

            else:
                                    
                return render(request, "login_cliente.html", {"cliente":cliente, "tipo_pedido":'tarde', "hoy":now, "ultimo":pedido}) 

    else:

        mensaje="No has ingresado nada"

    return HttpResponse(mensaje)


def menus_v(request):
    num_menus=request.GET["num_menus"]


    return HttpResponse(num_menus)
    #return render(request, "platos.html")

def platos_v(request):

    if request.method=="POST":
        num_registros=request.POST["num_hidden[]"]
        arr_para_insertar = []
        x = 0
        while x < int(num_registros):

            arr_para_insertar.append(x)
            plato=Platos(nombre=request.POST["nombre_" + str(x)],precio=request.POST["precio_plato_" + str(x)],tipo=request.POST["tipo_plato_" + str(x)],vigente='1')
            plato.save()
            x += 1

        return HttpResponse('Se insertaron todos los datos') 

    num_platos=request.GET["num_platos"]    
    arr = []
    i = 0
    while i < int(num_platos):
        arr.append(i)
        i += 1
        
    return render(request, "platos.html", {"arr_num_platos":arr})      

def ver_pedidos_v(request):    


    return HttpResponse('vean todos los pedidos')
    #return render(request, "platos.html")
