from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    portfolio = models.URLField(blank = True)
    profile_pic = models.ImageField(upload_to = 'pics', blank = True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username
