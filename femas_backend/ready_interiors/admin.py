from django.contrib import admin

from .models import *


class PhotoInline(admin.StackedInline):
    model = InteriorPhoto
    extra = 1
    show_change_link = True


class InteriorAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]


admin.site.register(Interior, InteriorAdmin)
