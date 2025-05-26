from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# Blog post endpoints
router.register('blog-posts', views.BlogPostViewSet)

# Contact form submission endpoint
router.register('contact', views.ContactViewSet, basename='contact')

urlpatterns = router.urls
