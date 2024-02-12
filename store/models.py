from django.db import models
from django.urls import reverse
from category.models import Category
# Create your models here.
class Store(models.Model):

    product_name = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.CharField(max_length=200, blank=True)
    price = models.IntegerField()
    Images = models.ImageField(upload_to='photo/products')
    stock = models.IntegerField()
    is_available  = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


    def get_url(self):
        return reverse('product_details', kwargs={"slug_category":self.category.Slug, "slug_product": self.slug})

    def __str__(self):
        return self.product_name