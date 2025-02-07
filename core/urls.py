from django.contrib import admin
from django.urls import path
from home.views import *

urlpatterns = [
    path('', index),
    path('productdetail/<int:id>/', product_detail),
    path('products/', ProductAPI.as_view()),
    path('product/<int:id>/', ProductDetailAPI.as_view()),
    path('admin/', admin.site.urls),
]
