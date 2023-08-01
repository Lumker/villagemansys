from django.contrib import admin
from .models import *

@admin.register(DistrictMunicipality, Municipality , Resident, Village, Household,)
class ResidentAdmin(admin.ModelAdmin):
    pass