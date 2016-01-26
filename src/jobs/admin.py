from django.contrib import admin

from .models import (Job,
                     Location,
                     Employer,
                     PositionMatch,
                     LocationMatch,
                     EmployerMatch)


class JobAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    fields = ["name"]


class LocationAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    fields = ["name"]


class EmployerAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    fields = ["name"]


admin.site.register(Job, JobAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Employer, EmployerAdmin)
admin.site.register(PositionMatch)
admin.site.register(LocationMatch)
admin.site.register(EmployerMatch)
