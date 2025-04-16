from django.urls import path
from . import views

urlpatterns = [
    path('blog-posts/', views.BlogPostListAPIView.as_view()),
]
