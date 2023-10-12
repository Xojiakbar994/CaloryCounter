from django.urls import path

from .views import (
    ProductCreateView,
    APIFoodsListView,
    APIFoodsUpdateList,
    APIFoodsCreateAPIView,
    APIFoodsDeleteAPIView,
)

urlpatterns = [
    path("new/", ProductCreateView.as_view(), name="new_food"),
    path("getFoodsList/<str:txt>/", APIFoodsListView.as_view()),
    path("update/<int:pk>", APIFoodsUpdateList.as_view()),
    path("insert/", APIFoodsCreateAPIView.as_view()),
    path("delete/<int:pk>", APIFoodsDeleteAPIView.as_view()),
]
