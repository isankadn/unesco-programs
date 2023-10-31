from django.contrib import admin
from .models import UnescoProgram


@admin.register(UnescoProgram)
class UnescoProgramAdmin(admin.ModelAdmin):
    list_display = ('description',)
    filter_horizontal = ('courses',)
