from django.contrib import admin

from .models import *


class SofaOptionInline(admin.StackedInline):
    model = SofaOption
    extra = 3
    show_change_link = True


class SofaAdmin(admin.ModelAdmin):
    inlines = [SofaOptionInline]


admin.site.register(Sofa, SofaAdmin)
admin.site.register(Table)
admin.site.register(Bed)
admin.site.register(Armchair)
admin.site.register(Chair)
admin.site.register(Kitchenware)
admin.site.register(Accessory)
