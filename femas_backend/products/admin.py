from django.contrib import admin

from .models import *


admin.site.register(Product)
admin.site.register(ProductPhoto)
admin.site.register(ProductVideo)
admin.site.register(ProductOption)
admin.site.register(ProductOptionChoice)
