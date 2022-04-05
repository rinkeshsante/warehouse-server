from django.contrib import admin

from .models import Package


class PackageAdmin(admin.ModelAdmin):
    list_display = (id, 'location_X', 'location_Y', 'done_processing')


admin.site.register(Package, PackageAdmin)
