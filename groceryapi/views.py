from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from .models import Product
from .models import User
from .models import TransactionStory
from .serializers import ProductsSerializer, TransactionStorySerializer, UserSerializer
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TransactionStoryViewSet(viewsets.ModelViewSet):
    queryset = TransactionStory.objects.all()
    serializer_class = TransactionStorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer



# def index(request):
#     return HttpResponse("Hello, world!")

# def get_product_by_id(self, product_id):
#     data = serializers.serialize("json", Product.objects.filter(id = product_id))
#     return HttpResponse(data)

# def get_user_by_id(self, user_id):
#     data = serializers.serialize("json", User.objects.filter(id=user_id))
#     return HttpResponse(data)

# def get_user_by_customer_id(self, customer_id):
#     data = serializers.serialize("json", User.objects.filter(customer_id=customer_id))
#     return HttpResponse(data)

# def get_transactions_story_by_customer_id(self, customer_id):
#     data = serializers.serialize("json", TransactionStory.objects.filter(customer_id=customer_id))
#     return JsonResponse({"data" : data  })

# class ProductViewSet(viewsets.ModelViewSet):

    # Create your views here.