from django.db import models
from nomenclature.models import Variable
from location.models import Location

# Create your models here.
class Scenario(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Plan(models.Model):
    year = models.IntegerField()
    variable = models.ForeignKey(Variable, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.year} - {self.variable}"