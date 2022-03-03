from rest_framework import routers
from apps.produse.api import ProductViewSet, ImageViewSet

router = routers.DefaultRouter()
router.register('produse/images', ImageViewSet, basename='image')
router.register('produse', ProductViewSet, basename='product')

urlpatterns = router.urls