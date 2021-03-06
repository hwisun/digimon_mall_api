from rest_framework.routers import DefaultRouter

from ..api import views

router = DefaultRouter()
router.register('', views.ListViewSet)

urlpatterns = router.urls
