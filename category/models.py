from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=100, unique=True)
    Slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_photo =  models.ImageField(upload_to='photo/categories', blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_url(self):
        return reverse('product_by_category', kwargs={"slug_category":self.Slug})

    def __str__(self):
        return self.cat_name