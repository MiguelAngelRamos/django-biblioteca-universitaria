from django import forms
from .models import Estudiante, Libro, Editorial

class EditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ej. Editorial Planeta',
                'autocomplete': 'off'
            }),
        }
        labels = {'nombre': 'Nombre de la Editorial'}

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['matricula', 'nombre_completo']
        widgets = {
            'matricula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 2026A123', 'autocomplete': 'off'}),
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre Completo del Estudiante', 'autocomplete': 'off'}),
        }
        labels = {'matricula': 'Matrícula Universitaria', 'nombre_completo': 'Nombre y Apellido'}

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'editorial', 'stock_disponible']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Fundamentos de Bases de Datos API'}),
            'editorial': forms.Select(attrs={'class': 'form-select'}),
            'stock_disponible': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }