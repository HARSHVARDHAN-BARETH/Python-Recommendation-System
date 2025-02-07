from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import Products
# Sonata 8943YL03 Yuva Gold Analog Watch  - For Women - Buy Sonata 8943YL03 Yuva Gold Analog Watch  - For Women  8943YL03 Online at Rs.780 in India Only at Flipkart.com. Round Dial, White Strap, Water Resistant, Buckle Clasp - Great Discounts, Only Genuine Products, 30 Day Replacement Guarantee, Free Shipping. Cash On Delivery!


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