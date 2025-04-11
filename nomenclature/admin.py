from django.contrib import admin
from .models import VariableGroup, Variable

# Register your models here.
admin.site.site_header = "Nomenclature Admin"
admin.site.site_title = "Nomenclature Admin Portal"
admin.site.index_title = "Welcome to the Nomenclature Admin Portal"

admin.site.register(VariableGroup)
admin.site.register(Variable)

