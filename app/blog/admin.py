from django.contrib import admin

from blog.models.posts import Post
from blog.models.profiles import Profile


admin.site.register(Post)
admin.site.register(Profile)
