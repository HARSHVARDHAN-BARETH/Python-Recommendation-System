from django.shortcuts import render
from rest_framework import serializers

from .models import Products

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
   
