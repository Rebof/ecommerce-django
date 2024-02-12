from django.contrib import admin
from .models import Store
# Register your models here.


class StoreAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'stock', 'price','category','date_modified','is_available')
    prepopulated_fields = {'slug': ('product_name',)}


admin.site.register(Store, StoreAdmin)