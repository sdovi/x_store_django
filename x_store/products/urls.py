from django.urls import path
from .views import CategoryListCreateAPIView, ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
]
