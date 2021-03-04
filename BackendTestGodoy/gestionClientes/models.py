from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    direccion=models.CharField(max_length=300)
    email=models.EmailField(blank=True, null=True)
    celular=models.CharField(max_length=12)
    rut=models.CharField(max_length=12)
    group=models.CharField(max_length=100)
    vigente=models.BooleanField()

    def __str__(self):
        return 'Nombre %s, Apellido %s, Direccion %s, Email %s, Celular %s, Rut %s, Group %s, Vigente %s' % (self.nombre, self.apellido, self.direccion, self.email, self.celular, self.rut, self.group, self.vigente)

class Platos(models.Model):
    nombre=models.CharField(max_length=100)
    precio=models.IntegerField()    
    tipo=models.CharField(max_length=100)   
    vigente=models.BooleanField()

    def __str__(self):
        return 'Nombre %s, Precio %s, Tipo %s, Vigente %s' % (self.nombre, self.precio, self.tipo, self.vigente)

class Menus(models.Model):
    id_platos=models.IntegerField()
    nombre=models.CharField(max_length=100)            
    fecha=models.DateField()
    vigente=models.BooleanField()

    def __str__(self):
        return 'Id platos %s, Nombre %s, Fecha %s, Vigente %s' % (self.id_platos, self.nombre, self.fecha, self.vigente)

class Pedidos(models.Model):
    id_comida=models.IntegerField()
    id_cliente=models.IntegerField()
    detalle=models.CharField(max_length=300)
    fecha=models.DateTimeField()
    vigente=models.BooleanField()

    def __str__(self):
        return 'Id_comida %s, Id_cliente %s, Fecha %s, Vigente %s' % (self.id_comida, self.id_cliente, self.fecha, self.vigente)
