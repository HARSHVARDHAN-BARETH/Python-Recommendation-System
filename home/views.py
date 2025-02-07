# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import Products
# from .serializer import productSerializer
# from .product_recomender import get_similar_product

# # Create your views here.
# class ProductAPI(APIView):
#     def get(self, request):
#         products = Products.objects.all().order_by('?')[:40]
#         serializer = productSerializer(products, many=True)
#         similar_products = get_similar_product(id, 10)
#         similar_products_serializer = productSerializer(similar_products, many = True)
#         return Response({
#             "all_products":serializer.data,
#             "similar_product": similar_products_serializer.data
#         })
        
# class ProductDetailAPI(APIView):
#     def get(self, request, id):
#         products = Products.objects.get(id=id)
#         serializer = productSerializer(products)
#         return Response({
#             "product": serializer.data
#         })
        
# def index(request):
#     return render(request, "index.html")
# def product_detail(request):
#     context = {'id':id}
#     return render(request, "productdetail.html", context)

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Products
from .serializer import productSerializer
from .product_recomender import get_similar_product

class ProductAPI(APIView):
    def get(self, request):
        products = Products.objects.all().order_by('?')[:5]
        serializer = productSerializer(products, many=True)
        return Response({
            "all_products": serializer.data
        })

class ProductDetailAPI(APIView):
    def get(self, request, id):
        product = Products.objects.get(id=id)
        similar_products = get_similar_product(id, 10)
        similar_products_serializer = productSerializer(similar_products, many=True)
        serializer = productSerializer(product)
        return Response({
            "product": serializer.data,
            "similar_products": similar_products_serializer.data
        })

def index(request):
    return render(request, "index.html")

def product_detail(request, id):
    context = {'id': id}
    return render(request, "productdetail.html", context)
