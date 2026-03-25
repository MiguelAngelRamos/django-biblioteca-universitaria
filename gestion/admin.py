from django.contrib import admin
from .models import Editorial, Estudiante, Credencial, Libro, Prestamo
# Register your models here.

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nombre_completo')
    search_fields = ('matricula', 'nombre_completo')

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'editorial', 'stock_disponible')
    list_filter = ('editorial',)
    search_fields = ('titulo',)

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'libro', 'fecha_prestamo', 'estado', 'multa_generada')
    list_filter = ('estado', 'fecha_prestamo')

admin.site.register(Editorial)
admin.site.register(Credencial)