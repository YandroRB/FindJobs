from django.db import models

class Trabajo(models.Model):
    id = models.AutoField(primary_key= True)
    titulo= models.CharField(max_length=30)
    descripcion=models.TextField(blank=True,null=True)
    ubicacion= models.CharField(max_length=30)
    empresa=models.CharField(max_length= 50)
    tipo=models.CharField(max_length=30)
    area=models.CharField(max_length=40)
    fecha=models.DateTimeField(auto_now=True)
