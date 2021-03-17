from django.contrib import admin
from .models import plugin_crossconnect

@admin.register(plugin_crossconnect)
class plugin_crossconnectadmin(admin.ModelAdmin):
    #list_display = ("customer")
    list_display = ("customer","col2")