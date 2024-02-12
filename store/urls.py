
from django.urls import path
from . import views
from django.conf.urls.static import  static


urlpatterns = [
    path('', views.store, name='store'),
    path('<slug:slug_category>', views.store, name='product_by_category'),
    path('<slug:slug_category>/<slug:slug_product>/', views.product_details, name='product_details'),
] 
