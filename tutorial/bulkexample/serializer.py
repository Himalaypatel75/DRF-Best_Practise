
from rest_framework import serializers  
from bulkexample import models  
  
# class ProductSerializer(serializers.ModelSerializer):  
#     class Meta:  
#         model = models.Product  
#         fields = ["id", "title", "description", "price", "type", "visible", "discount", "created_at", "updated_at"]  

class ProductBulkCreateUpdateSerializer(serializers.ListSerializer):  
    def create(self, validated_data):  
        product_data = [models.Product(**item) for item in validated_data]  
        # return models.Product.objects.bulk_create(product_data) 
        return models.Product.objects.bulk_create(product_data)  
  
  
class ProductSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = models.Product  
        fields = ["id", "title", "description", "price", "type", "visible", "discount", "created_at", "updated_at"]  
        read_only_fields = ['id',]  
        list_serializer_class = ProductBulkCreateUpdateSerializer 