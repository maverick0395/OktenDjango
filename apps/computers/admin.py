from django.contrib import admin

from .models import ComputerModel


@admin.register(ComputerModel)
class ComputerAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'ram', 'screen')