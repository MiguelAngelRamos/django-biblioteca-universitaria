from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection 
from django.views.generic import ListView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Estudiante, Libro, Prestamo, Credencial, Editorial
from .forms import EstudianteForm, LibroForm, EditorialForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import View

# =====================================================================
# 1. Vistas Genéricas y ORM (CRUD BÁSICO)
# =====================================================================
class EstudianteListView(ListView):
    model = Estudiante
    template_name = 'gestion/estudiante_list.html'
    context_object_name = 'estudiantes'

class LibroListView(ListView):
    model = Libro
    template_name = 'gestion/libro_list.html'
    context_object_name = 'libros'
    queryset = Libro.objects.all().prefetch_related('estudiantes', 'editorial') # Optimización M:N

class EstudianteCreateView(SuccessMessageMixin, CreateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'gestion/estudiante_form.html'
    success_url = reverse_lazy('estudiante_list')
    success_message = "¡Estudiante y Credencial creados exitosamente!"

    def form_valid(self, form):
        response = super().form_valid(form)
        # Construye la credencial automáticamente en BD
        Credencial.objects.create(
            estudiante=self.object,
            codigo_barras=f"CRED-{self.object.matricula}",
            activa=True
        )
        return response

class LibroCreateView(SuccessMessageMixin, CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'gestion/libro_form.html'
    success_url = reverse_lazy('libro_list')
    success_message = "¡Nuevo libro registrado nativamente!"

class EditorialCreateView(SuccessMessageMixin, CreateView):
    model = Editorial
    form_class = EditorialForm
    template_name = 'gestion/editorial_form.html'
    success_url = reverse_lazy('libro_create')
    success_message = "¡Editorial añadida!"

# =====================================================================
# 2. Vistas Especiales con SQL Crudo y Stored Procedures
# =====================================================================
class ReporteSQLCrudoView(ListView):
    template_name = 'gestion/reporte_raw_sql.html'
    context_object_name = 'libros'

    def get_queryset(self):
        query = '''
            SELECT l.* 
            FROM gestion_libro l
            INNER JOIN gestion_prestamo p ON l.id_libro = p.libro_id
            WHERE p.estado = 'Activo'
        '''
        return Libro.objects.raw(query)
    
class EjecutarProcedimientoView(View):
    def get(self, request, estudiante_id, *args, **kwargs):
        """ Invoca procedimiento almacenado usando Cursor """
        with connection.cursor() as cursor:
            try:
                cursor.callproc('sp_calcular_multa', [estudiante_id])
                messages.success(request, f'¡SP de PostgreSQL ejecutado! Multas calculadas para ID {estudiante_id}.')
            except Exception as e:
                messages.error(request, f'Error al ejecutar el procedimiento en PostgreSQL: {str(e)}')
                
        return redirect('estudiante_list')
# def reporte_sql_crudo(request):
#     """ SQL .raw() Puro """
#     query = '''
#         SELECT l.* 
#         FROM gestion_libro l
#         INNER JOIN gestion_prestamo p ON l.id_libro = p.libro_id
#         WHERE p.estado = 'Activo'
#     '''
#     libros_prestados = Libro.objects.raw(query)
#     return render(request, 'gestion/reporte_raw_sql.html', {'libros': libros_prestados})

# def ejecutar_procedimiento_cursor(request, estudiante_id):
#     """ Invoca procedimiento almacenado usando Cursor """
#     with connection.cursor() as cursor:
#         try:
#             cursor.callproc('sp_calcular_multas', [estudiante_id])
#             messages.success(request, f'¡SP de PostgreSQL ejecutado! Multas calculadas para ID {estudiante_id}.')
#         except Exception as e:
#             messages.error(request, f'Error al ejecutar el procedimiento en PostgreSQL: {str(e)}')
            
#     return redirect('estudiante_list')