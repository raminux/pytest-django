from django.contrib import admin
from companies import models

@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    pass
