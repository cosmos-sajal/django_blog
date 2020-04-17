from django.urls import path
from blog.views import home, about, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/new/', PostCreateView.as_view(), name='blog-post-create'),
    path('post/<str:uuid>/', PostDetailView.as_view(), name='blog-post-detail'),
    path('post/<str:uuid>/update/',
         PostUpdateView.as_view(), name='blog-post-update'),
    path('post/<str:uuid>/delete/',
         PostDeleteView.as_view(), name='blog-post-delete'),
    path('about/', about, name='blog-about')
]
