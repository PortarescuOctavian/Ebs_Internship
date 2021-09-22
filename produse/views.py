from rest_framework.viewsets import ModelViewSet

from .models import Product
from .serializers import ProductSerializer, ImageSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self,request):
        queryset = Product.objects.all()
        paginator = PageNumberPagination()
        paginated_result = paginator.paginate_queryset(queryset,request)
        serializer = ProductSerializer(paginated_result, many=True)
        return Response(serializer.data)
        
class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer