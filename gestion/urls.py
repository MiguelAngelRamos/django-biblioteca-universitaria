from django.urls import path
from . import views

urlpatterns = [
    # 1. ORM Standard Vistas Base
    path('', views.LibroListView.as_view(), name='libro_list'),
    path('estudiantes/', views.EstudianteListView.as_view(), name='estudiante_list'),
    path('estudiantes/nuevo/', views.EstudianteCreateView.as_view(), name='estudiante_create'),
    path('libros/nuevo/', views.LibroCreateView.as_view(), name='libro_create'),
    path('editoriales/nueva/', views.EditorialCreateView.as_view(), name='editorial_create'),
    
    # 2. Consultas Personalizadas / Raw SQL
    # path('reporte-avanzado/', views.reporte_sql_crudo, name='reporte_avanzado'),
    
    # 3. Invocación segura de SP's y Cursores
    # path('ejecutar-sp/<int:estudiante_id>/', views.ejecutar_procedimiento_cursor, name='ejecutar_sp'),
]