from django.urls import path
from rest_framework.routers import DefaultRouter
from products.views import ProductViewset, CategoriesView, BrandsView

product_router = DefaultRouter()
product_router.register('products',ProductViewset, basename="products")

urlpatterns = [
    path("categories/", CategoriesView.as_view()),
    path("brands/", BrandsView.as_view())
]

urlpatterns+=product_router.urls