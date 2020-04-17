from django.db import models
from django.contrib.auth.models import User

from blog.models.base import BaseModel


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile.pics')

    def __str__(self):
        return f'{self.user.username} Profile'
