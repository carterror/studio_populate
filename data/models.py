from django.db import models
from nomenclature.models import Variable
from location.models import Location

# Create your models here.
class Measurement(models.Model):
    id_variable = models.ForeignKey(Variable, on_delete=models.CASCADE)
    id_localidad = models.ForeignKey(Location, on_delete=models.CASCADE)
    fecha = models.DateField()
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    fuente_dato = models.CharField(max_length=100, blank=True, null=True)
    confiabilidad = models.CharField(max_length=20, blank=True, null=True)  # Ej: Alta, Media, Baja
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    usuario_ingreso = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.id_variable} - {self.fecha}"