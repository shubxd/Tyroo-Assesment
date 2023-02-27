from rest_framework.viewsets import ModelViewSet
from products.seriallizers import ProductSerializer, CategorySerialzer, BrandSerializer
from rest_framework.permissions import IsAuthenticated
from products.models import Product, Categories, Brand
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django.db.models import Q


class ProductViewset(ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter,]
    search_fields = ['brand__name', 'name']

    def get_queryset(self):
        query_params = self.request.query_params
        price_range = query_params.get('price_range').split(',') if  query_params.get('price_range') else None
        brands = query_params.get('brands').split(',') if query_params.get('brands') else None

        price_filter = Q()
        if price_range:
            price_filter = Q(price__range=price_range)
        
        brand_filter = Q()
        if brands:
            brand_filter = Q(brand__name__in=brands)
        
        query_set = Product.objects.filter(
            price_filter,
            brand_filter
        )
        return query_set

class CategoriesView(APIView):
    serializer_class = CategorySerialzer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = Categories.objects.all()
        return Response(self.serializer_class(data, many=True).data)

class BrandsView(ListAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    permission_classes = [IsAuthenticated]







