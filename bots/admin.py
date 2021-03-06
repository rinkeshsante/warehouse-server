from django.contrib import admin
from .models import Bot


class BotAdmin(admin.ModelAdmin):
    list_display = ('reg_id', 'location_X', 'location_Y')


admin.site.register(Bot, BotAdmin)
