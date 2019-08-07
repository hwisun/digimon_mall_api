from rest_framework.routers import DefaultRouter

from ..api import views

router = DefaultRouter()
router.register('', views.UserViewSet)

urlpatterns = router.urls
