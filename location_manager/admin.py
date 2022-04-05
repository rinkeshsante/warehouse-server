from django.contrib import admin

from .models import LoactionManger


class LoactionMangerAdmin(admin.ModelAdmin):
    list_display = (id, 'postal_address', 'is_full')


admin.site.register(LoactionManger, LoactionMangerAdmin)
