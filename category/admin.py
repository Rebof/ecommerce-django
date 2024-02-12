from django.contrib import admin
from .models import Category
# Register your models here.





class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'Slug'  : ('cat_name',)}  # When creating an object, a slug will be created from the name field value.
    list_display = ('cat_name', 'Slug')






admin.site.register(Category, CategoryAdmin)