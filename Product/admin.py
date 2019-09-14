from django.contrib import admin

from .models import menubar, Product, Product_feature, Product_image
# Register your models here.
admin.site.register(Product)
admin.site.register(menubar)
admin.site.register(Product_feature)
admin.site.register(Product_image)

