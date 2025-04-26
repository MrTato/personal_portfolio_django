from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # path('blog-posts/', views.BlogPostListAPIView.as_view()),
]

router = DefaultRouter()
router.register('blog-posts', views.BlogPostViewSet)
urlpatterns += router.urls