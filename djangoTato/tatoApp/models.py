from email.policy import default
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.forms import BooleanField

# Create your models here.

class Messages(models.Model):
    content = models.TextField(max_length=180)
    response = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    
class Materias(models.Model):
    title = models.TextField(max_length=180)
    descripcion = models.TextField(max_length=1000)
    image = models.ImageField(null=True, blank=True, upload_to='materiasImages')
    
class MateriasConstrucciones(models.Model):
    title = models.TextField(max_length=180)
    descripcion = models.TextField(max_length=1000)
    image = models.ImageField(null=True, blank=True, upload_to='materiasConstImages')
    
class Instalaciones(models.Model):
    title = models.TextField(max_length=180)
    descripcion = models.TextField(max_length=1000)
    foto1 = models.ImageField(null=True, blank=True, upload_to='instalacionesImages')
    foto2 = models.ImageField(null=True, blank=True, upload_to='instalacionesImages')
    foto3 = models.ImageField(null=True, blank=True, upload_to='instalacionesImages')
    
class Proyectos(models.Model):
    title = models.TextField(max_length=180)
    descripcion = models.TextField(max_length=1000)
    videoLink = models.CharField(null=True, max_length=300)