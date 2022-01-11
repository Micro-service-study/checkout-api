from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .api.serializers import OrderSerializer
from .kafka.producer.producer import brokerProducer

@api_view(['POST'])
def checkout(request):
  if request.method == 'POST':
    serialize = OrderSerializer(data=request.data)
    serialize.is_valid(raise_exception=True)
    brokerProducer("checkout-check-request", request.data)
    return Response(serialize.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def checkoutDetails(request):
  serialize = OrderSerializer(data=request.data)
  serialize.is_valid(raise_exception=True)
    
  return Response(serialize.data, status=status.HTTP_201_CREATED)