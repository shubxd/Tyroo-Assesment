from rest_framework import serializers
from products.models import Product, Categories, Brand

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Product

class CategorySerialzer(serializers.ModelSerializer):

    id = serializers.IntegerField()
    name = serializers.CharField()
    type = serializers.IntegerField()
    type_name = serializers.SerializerMethodField()


    class Meta:
        fields = (
            "id",
            "name",
            "type",
            "type_name"
        )
        model = Categories
    
    def get_type_name(self, obj):
        prod_types = dict(obj.PRODUCT_TYPES)
        return prod_types.get(obj.type)

class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Brand