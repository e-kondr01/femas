from django.contrib import admin
from django.contrib.auth.models import User, Group
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


class ProductAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, VideoInline]


admin.site.register(Sofa, SofaAdmin)
admin.site.register(Table, ProductAdmin)
admin.site.register(Bed, ProductAdmin)
admin.site.register(Armchair, ProductAdmin)
admin.site.register(Chair, ProductAdmin)
admin.site.register(Kitchenware, ProductAdmin)
admin.site.register(Accessory, ProductAdmin)
#  admin.site.register(ProductVersion)

admin.site.unregister(User)
admin.site.unregister(Group)
