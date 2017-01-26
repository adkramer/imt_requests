from django.contrib import admin

# Register your models here.
from .models import Uom, Manufacturer, Vendor, ItemRequest

@admin.register(Uom)
class  UomAdmin(admin.ModelAdmin):
    pass

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    pass

@admin.register(ItemRequest)
class ItemRequestAdmin(admin.ModelAdmin):
    pass
