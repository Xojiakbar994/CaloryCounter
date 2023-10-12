from django.shortcuts import render
from django.views.generic import CreateView

from rest_framework.generics import (
    ListAPIView,
    UpdateAPIView,
    CreateAPIView,
    DestroyAPIView,
)

from .models import Products
from .serializers import ProductsSerializer


# Create your views here.
class ProductCreateView(CreateView):
    model = Products
    template_name = "food/new.html"
    fields = "__all__"
    success_url = "/"


class APIFoodsListView(ListAPIView):
    serializer_class = ProductsSerializer
    template_name = "home.html"

    def get_queryset(self):
        txt = self.kwargs["txt"]
        queryset = Products.objects.filter(product_name__icontains=txt)
        return queryset


class APIFoodsUpdateList(UpdateAPIView):
    queryset = Products.objects.all
    serializer_class = ProductsSerializer


class APIFoodsCreateAPIView(CreateAPIView):
    pass


class APIFoodsDeleteAPIView(DestroyAPIView):
    pass
