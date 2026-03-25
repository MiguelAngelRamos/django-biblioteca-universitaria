from django.db import models


class Editorial(models.Model):
    id_editorial = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    
    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    id_estudiante = models.BigAutoField(primary_key=True)
    matricula = models.CharField(max_length=20, unique=True)
    nombre_completo = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_completo

# RELACIÓN 1 A 1
class Credencial(models.Model):
    estudiante = models.OneToOneField(Estudiante, on_delete=models.CASCADE, related_name="credencial")
    codigo_barras = models.CharField(max_length=50, unique=True)
    fecha_expedicion = models.DateField(auto_now_add=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return f"Credencial: {self.codigo_barras} de {self.estudiante.nombre_completo}"

# RELACIÓN 1 A MUCHOS Y MUCHOS A MUCHOS
class Libro(models.Model):
    id_libro = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    
    # 1:N
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, related_name="libros")
    stock_disponible = models.IntegerField(default=1)

    # N:M (usamos through para romper la relación hacia Prestamo)
    estudiantes = models.ManyToManyField(Estudiante, through='Prestamo', related_name='libros_prestados')

    def __str__(self):
        return self.titulo

# TABLA INTERMEDIA (Rompiendo el Muchos a Muchos)
class Prestamo(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    
    fecha_prestamo = models.DateTimeField(auto_now_add=True)
    fecha_devolucion = models.DateTimeField(null=True, blank=True)
    estado = models.CharField(max_length=20, default='Activo')
    
    multa_generada = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Prestamo: {self.estudiante} - {self.libro} ({self.estado})"