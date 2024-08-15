from rest_framework.routers import DefaultRouter
from authentication.views.user import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = router.urls
