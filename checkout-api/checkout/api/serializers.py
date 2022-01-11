from rest_framework import serializers

class OrderSerializer(serializers.Serializer):
  value_order = serializers.FloatField()
  email = serializers.EmailField()
  name = serializers.CharField()  
  product_id = serializers.CharField()
  
  class Meta:
    fields = (
      'value_order', 
      'email', 
      'name', 
      'product_id'
    )
    abstract = True