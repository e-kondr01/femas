from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from .models import *


class SofaOptionInline(admin.StackedInline):
    model = SofaOption
    extra = 1
    show_change_link = True


class PhotoInline(GenericStackedInline):
    model = ProductPhoto
    extra = 1
    show_change_link = True


class VideoInline(GenericStackedInline):
    model = ProductVideo
    extra = 1
    show_change_link = True


class SofaAdmin(admin.ModelAdmin):
    inlines = [SofaOptionInline, PhotoInline, VideoInline]


admin.site.register(Sofa, SofaAdmin)
admin.site.register(Table)
admin.site.register(Bed)
admin.site.register(Armchair)
admin.site.register(Chair)
admin.site.register(Kitchenware)
admin.site.register(Accessory)
admin.site.register(ProductVersion)
