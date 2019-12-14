from articles.api.views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', ArticleViewSet, basename='ArticlesApi')
urlpatterns = router.urls