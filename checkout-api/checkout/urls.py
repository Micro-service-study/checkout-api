from django.urls import path

from .views import checkout, checkoutDetails

urlpatterns = [
  path('checkout/', checkout),
  path('checkout/check', checkoutDetails),
]