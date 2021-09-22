from .models import Product, Image
from rest_framework import viewsets, permissions
from .serializers import ProductSerializer, ImageSerializer

class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	permission_classes = [
		permissions.AllowAny
	]
	serializer_class = ProductSerializer

class ImageViewSet(viewsets.ModelViewSet):
	queryset = Image.objects.all()
	permission_classes = [
		permissions.AllowAny
	]
	serializer_class = ImageSerializer