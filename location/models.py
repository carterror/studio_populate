from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, blank=True, null=True)  # Ex: Municipality, Province
    code = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name