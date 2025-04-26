from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('blog-posts', views.BlogPostViewSet)
urlpatterns = router.urls