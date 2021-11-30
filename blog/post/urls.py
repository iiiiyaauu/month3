from django.urls import path
from . import views
urlpatterns = [
    path('', views.PostListView.as_view()),
    path('create/', views.create_blog_view),
    path('<int:pk>/', views.PostDetailView.as_view())
]
