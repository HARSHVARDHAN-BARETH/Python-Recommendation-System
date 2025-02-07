import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'
django.setup()
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from home.models import Products


# import random
# from faker import Faker


# import csv
# csv_file_path = 'flipkart_com-ecommerce_sample.csv'
# from home.models import *

# with open(csv_file_path, mode='r', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         try:
#             product_name = row['product_name']
#             product_image = eval(row['image'])[0]
#             description = row['description']
#             category = row['product_category_tree'].split('>>')[0].strip('[]"')
#             price = row['retail_price']
            
#             print (
#                 product_name,
#                 product_image,
#                 description,
#                 category,
#                 price
#             )
            
#             Products.objects.update_or_create(
#                 name=product_name,
#                 defaults={
#                     'product_image': product_image,
#                     'description': description,
#                     'category': category,
#                     'price': price
#                 }
#             )
            
#         except Exception as e:
#             print(e)
            
# print("Products imported Successfully!")

def get_similar_product(product_id, top_n=10):
    vectorizer = TfidfVectorizer(stop_words="english")
    product_description = Products.objects.all().values_list('description', flat=True)
    tfd_matrix = vectorizer.fit_transform(product_description)
    print(tfd_matrix)
    target_product = Products.objects.get(id = product_id)
    all_products = list(Products.objects.all())
    target_index = all_products.index(target_product)
    cosine_sim = cosine_similarity(tfd_matrix[target_index], tfd_matrix).flatten()
    similar_indicies = cosine_sim.argsort()[-top_n-1:-1][::-1]
    similar_indicies = [i for i in similar_indicies if i != target_index]
    similar_product = []
    for idx in similar_indicies:
        similar_product.append(all_products[idx])
    print(type(similar_indicies))
    return similar_product
    
print(get_similar_product(2616))