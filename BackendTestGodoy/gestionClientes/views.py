from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from gestionClientes.models import Clientes, Pedidos, Platos, Menus, Opciones
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.

def suma(x, y):

    return x + y
@login_required
def product_detail(request, pk):
    plato = get_object_or_404(Platos, pk=pk)

    return render(request, 'plato_detalle.html', {'plato': plato})

def login(request):

    return render(request, "login_t.html")

def login_res(request):

    now=timezone.now()
    fecha_arr=[]
    anio=now.year
    fecha_arr.append(str(anio))
    mes=now.month
    fecha_arr.append(str(mes))
    hoy=now.day
    fecha_arr.append(str(hoy))

    if request.method=="POST":

        opcion = request.POST["select_opcion"]        
        comentario = request.POST["comentarios"]
        id_cliente = request.POST["id_cliente"]

        ped=Pedidos(id_cliente=id_cliente, fecha=now, vigente='1',detalle=comentario, date=now, opcion = 'Opcion '+opcion)                   
        
        ped.save()


        return HttpResponse('Se ingreso gestion Pedido')


    if request.GET["rut"]:

        #mensaje="Rut a buscar: %r" %request.GET["rut"]
        rut=request.GET["rut"]
        
        cliente=Clientes.objects.filter(rut=rut).first()

        
        
        
        if cliente.group == 'Admin':

            
            
            

            return render(request, "login_admin.html", {"cliente":cliente, "query":rut, "fecha_arr":fecha_arr})

        else:
            
            
            hoy=now.day
            cliente_id=cliente.id
            pedido=Pedidos.objects.filter(id_cliente=cliente_id,fecha__lte=now).order_by('fecha').last()
            opcion=Opciones.objects.filter(id=1)
            
            #se ocupa la tabla opcion para que Nora pueda cambiarlo mas facil en el futuro
            if now.hour < opcion[0].tope:
                
                if pedido == None:
                    #return HttpResponse(fecha_arr[1])
                    total_menus=Menus.objects.filter(fecha=fecha_arr[0]+'-'+fecha_arr[1]+'-'+fecha_arr[2],vigente=1).order_by('nombre')
                    
                    platos_vigentes=Platos.objects.filter(vigente=1).order_by('nombre')
                    #Menus.objects.filter(fecha="2021-03-05").delete()

                    for menu in total_menus:
                        ultimo=menu.nombre
                    split=ultimo.split()
                    
                    arreglo = []
                    arreglo_fragmento = []
                    i = 1
                    while i <= int(split[1]):
                        
                        arreglo_fragmento = []
                        for menu in total_menus:
                            
                            if menu.nombre == 'Opcion ' + str(i):
                                
                                for plato in platos_vigentes:
                                    if plato.id == menu.id_platos:
                                        arreglo_fragmento.append({'name': plato.nombre,'id_plato': plato.id, 'nombre_opcion': 'Opcion ' + str(i), 'fecha': menu.fecha}) 
                                

                        while len(arreglo_fragmento) < 4:    
                        
                            arreglo_fragmento.append({'name': 'Sin plato','id_plato': 0, 'nombre_opcion': 'Opcion ' + str(i), 'fecha': menu.fecha})    
                                
                            
                        arreglo.append(arreglo_fragmento)
                        i += 1      
                    
                    return render(request, "login_cliente.html", {"cliente":cliente, "tipo_pedido":'temprano', "hoy":now, "ultimo":pedido, "comio":0, "fecha_arr":fecha_arr,"arr_arreglo":arreglo,"platos_vigentes":platos_vigentes, "date_arr":fecha_arr[0]+'-'+fecha_arr[1]+'-'+fecha_arr[2]})
                                                          
                elif pedido.fecha.day == hoy:

                    return render(request, "login_cliente.html", {"cliente":cliente, "tipo_pedido":'temprano', "hoy":now, "ultimo":pedido, "comio":1})

                else:
                    #return HttpResponse(fecha_arr[1])
                    total_menus=Menus.objects.filter(fecha=fecha_arr[0]+'-'+fecha_arr[1]+'-'+fecha_arr[2],vigente=1).order_by('nombre')
                    
                    platos_vigentes=Platos.objects.filter(vigente=1).order_by('nombre')
                    #Menus.objects.filter(fecha="2021-03-05").delete()

                    for menu in total_menus:
                        ultimo=menu.nombre
                    split=ultimo.split()
                    
                    arreglo = []
                    arreglo_fragmento = []
                    i = 1
                    while i <= int(split[1]):
                        
                        arreglo_fragmento = []
                        for menu in total_menus:
                            
                            if menu.nombre == 'Opcion ' + str(i):
                                
                                for plato in platos_vigentes:
                                    if plato.id == menu.id_platos:
                                        arreglo_fragmento.append({'name': plato.nombre,'id_plato': plato.id, 'nombre_opcion': 'Opcion ' + str(i), 'fecha': menu.fecha}) 
                                

                        while len(arreglo_fragmento) < 4:    
                        
                            arreglo_fragmento.append({'name': 'Sin plato','id_plato': 0, 'nombre_opcion': 'Opcion ' + str(i), 'fecha': menu.fecha})    
                                
                            
                        arreglo.append(arreglo_fragmento)
                        i += 1      
                    
                    return render(request, "login_cliente.html", {"cliente":cliente, "tipo_pedido":'temprano', "hoy":now, "ultimo":pedido, "comio":0, "fecha_arr":fecha_arr,"arr_arreglo":arreglo,"platos_vigentes":platos_vigentes, "date_arr":fecha_arr[0]+'-'+fecha_arr[1]+'-'+fecha_arr[2]})

            else:
                                    
                return render(request, "login_cliente.html", {"cliente":cliente, "tipo_pedido":'tarde', "hoy":now, "ultimo":pedido}) 

    else:

        mensaje="No has ingresado nada"

    return HttpResponse(mensaje)


def menus_v(request):
    
    if request.method=="POST":
        
        num_opciones=request.POST["opcions_hidden"]
        num_platos=request.POST["platos_hidden"]
        date=request.POST["date"]

        x = 1
        while x <= int(num_opciones):
                        
            z = 0
            while z < int(num_platos):

                if int(request.POST["id_plato_" + str(x) + "_" + str(z)]) > 0:

                    men=Menus(id_platos=request.POST["id_plato_" + str(x) + "_" + str(z)],nombre="Opcion " + str(x),fecha=date,vigente='1')                   
                    men.save()

                z += 1

            x += 1

        return HttpResponse('Se ha ingresado el Menu') 

    num_menus=request.GET["num_menus"]    
    arr_opciones = []
    arr_platos = [0,1,2,3]
    i = 1
    while i <= int(num_menus):
        arr_opciones.append(i)
        i += 1
    
    platos_vigentes=Platos.objects.filter(vigente=1).order_by('nombre')

    return render(request, "menus.html", {"arr_num_opciones":arr_opciones,"arr_num_platos":arr_platos,"platos_vigentes":platos_vigentes})

def modificar_menus_v(request):
    
    if request.method=="POST":
        #Menus.objects.filter(fecha="2021-03-06").delete()
        #return HttpResponse(request.POST["opcions_hidden_nombre_1"])
                
        num_opciones=request.POST["mum_opcions_hidden"]        
        date=request.POST["date"]

        Menus.objects.filter(fecha=request.POST["date"]).delete()
        
        #return HttpResponse('se borro')

        x = 1
        while x <= int(num_opciones):                        
            z = 1
            while z <= int(4):

                if int(request.POST["id_plato_" + str(x) + "_" + str(z)]) > 0:

                    men=Menus(id_platos=request.POST["id_plato_" + str(x) + "_" + str(z)],nombre="Opcion " + str(x),fecha=date,vigente='1')                   
                    men.save()

                z += 1

            x += 1

        return HttpResponse('Se ha Modificado el Menu') 


    date=request.GET["date"]
    date_arr=date.split("-")    
    total_menus=Menus.objects.filter(fecha=date,vigente=1).order_by('nombre')
    platos_vigentes=Platos.objects.filter(vigente=1).order_by('nombre')
    #Menus.objects.filter(fecha="2021-03-05").delete()

    for menu in total_menus:
        ultimo=menu.nombre
    split=ultimo.split()

    arreglo = []
    arreglo_fragmento = []
    i = 1
    while i <= int(split[1]):
        
        arreglo_fragmento = []
        for menu in total_menus:
            
            if menu.nombre == 'Opcion ' + str(i):
                
                for plato in platos_vigentes:
                    if plato.id == menu.id_platos:
                       arreglo_fragmento.append({'name': plato.nombre,'id_plato': plato.id, 'nombre_opcion': 'Opcion ' + str(i), 'fecha': menu.fecha}) 
                

        while len(arreglo_fragmento) < 4:    
        
            arreglo_fragmento.append({'name': 'Sin plato','id_plato': 0, 'nombre_opcion': 'Opcion ' + str(i), 'fecha': menu.fecha})    
                
            
        arreglo.append(arreglo_fragmento)
        i += 1      

    return render(request, "modificar_menus.html", {"arr_arreglo":arreglo,"platos_vigentes":platos_vigentes, "date_arr":date_arr})

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
    
    fecha_seleccionada=request.GET["date"]
    now=timezone.now()
    
    pedidos=Pedidos.objects.filter(vigente='1',date=fecha_seleccionada).order_by('fecha')
    clientes=Clientes.objects.filter(vigente='1') 
    arreglo_pedidos_completos = []  

    for pedido in pedidos:
        if pedido.detalle == 'Escribe aquí su comida personalizada':
            detalle = ''
        else:
            detalle = 'con el detalle '+pedido.detalle
        for cliente in clientes:
            if pedido.id_cliente == cliente.id:
                arreglo_pedidos_completos.append({'name': cliente.nombre + " " + cliente.apellido,'id_cliente': pedido.id_cliente, 'nombre_opcion': pedido.opcion, 'fecha': pedido.date, 'detalle':detalle})
    
    return render(request, "listar_pedidos.html", {"pedidos":arreglo_pedidos_completos})


