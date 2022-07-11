
from rest_framework import serializers  
from bulkexample import models  
  
# class ProductSerializer(serializers.ModelSerializer):  
#     class Meta:  
#         model = models.Product  
#         fields = ["id", "title", "description", "price", "type", "visible", "discount", "created_at", "updated_at"]  

class ProductBulkCreateUpdateSerializer(serializers.ListSerializer):  
    def create(self, validated_data): 
        with_id = []
        print(validated_data)
        for item in validated_data:
            if not (item.get('id') is None):
                print(f"this is id>>{item}<<")
            else:
                print(f"this in non id>>{item}<<")
        product_data = [models.Product(**item) for item in validated_data]  
        # return models.Product.objects.bulk_create(product_data) 
        return models.Product.objects.bulk_create(product_data)  
  
class ProductSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = models.Product  
        fields =  ["id", "title", "description", "price", "type", "visible", "discount", "created_at", "updated_at"]  
        # list_serializer_class = ProductBulkCreateUpdateSerializer 

class ProductViewSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = models.Product  
        fields = ["id", "title", "description", "price", "type", "visible", "discount", "created_at", "updated_at"]  