from django.urls import path
from blog.views import home, about

urlpatterns = [
    path('', home, name='blog-home'),
    path('about/', about, name='blog-about')
]
