from django.contrib import admin

from .models import Profile, UserJob


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "slug"]
    fields = ["user", "location", "picture"]


admin.site.register(Profile, ProfileAdmin)

admin.site.register(UserJob)
