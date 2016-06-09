from django.contrib import admin

from .models import Tooltip


@admin.register(Tooltip)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ['name', 'header', 'is_activated']
    list_editable = ['is_activated']

    order_by = ['name']
