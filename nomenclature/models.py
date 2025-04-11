from django.db import models

# Create your models here.
class VariableGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Variable(models.Model):
    group = models.ForeignKey(VariableGroup, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    unit_of_measure = models.CharField(max_length=50, blank=True, null=True)
    variable_type = models.CharField(max_length=50, blank=True, null=True)  # Ex: 'Percentage', 'Total', 'Index'

    def __str__(self):
        return self.name