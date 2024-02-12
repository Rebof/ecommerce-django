from django.shortcuts import render , get_object_or_404
from .models import Store
from category.models import Category
# Create your views here.
def store(request, slug_category=None):
    categories = None
    products = None
    if slug_category != None:
        categories = get_object_or_404(Category, Slug=slug_category)
        
        products = Store.objects.filter(category=categories, is_available=True)
        
        p_count = products.count()
    else:
        products = Store.objects.all().filter(is_available=True)
        p_count = products.count()
    
    context={
        'products':products,
        'products_count': p_count
        }
    return render(request, 'store/storepage.html', context)

def product_details(request, slug_category, slug_product):
    try:
        product_det = Store.objects.get(category__Slug=slug_category, slug=slug_product)
    except Exception as e:
        raise e
    
    context = {
        'product_de' : product_det,
    }
    return  render ( request ,'store/product_details.html', context) 