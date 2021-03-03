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

class Comidas(models.Model):
    nombre=models.CharField(max_length=100)
    precio=models.IntegerField()
    detalle=models.CharField(max_length=300)
    flag=models.BooleanField()
    fecha=models.DateTimeField()
    vigente=models.BooleanField()

    def __str__(self):
        return 'Nombre %s, Precio %s, Detalle %s, Flag %s, Fecha %s, Vigente %s' % (self.nombre, self.precio, self.detalle, self.flag, self.fecha, self.vigente)

class Pedidos(models.Model):
    id_comida=models.IntegerField()
    id_cliente=models.IntegerField()
    fecha=models.DateTimeField()
    vigente=models.BooleanField()

    def __str__(self):
        return 'Id_comida %s, Id_cliente %s, Fecha %s, Vigente %s' % (self.id_comida, self.id_cliente, self.fecha, self.vigente)
