from django.contrib import admin
from .models import Messages, Materias, MateriasConstrucciones, Proyectos, Instalaciones
# Register your models here.

admin.site.register(Messages)
admin.site.register(Materias)
admin.site.register(MateriasConstrucciones)
admin.site.register(Proyectos)
admin.site.register(Instalaciones)
