from rest_framework import routers
from .api import ProductViewSet, ImageViewSet

router = routers.DefaultRouter()
router.register('api/produse/images/', ImageViewSet, 'produse/images')
router.register('api/produse', ProductViewSet, 'produse')

urlpatterns = router.urls