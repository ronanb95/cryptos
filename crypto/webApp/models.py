#SIDE NOTE: Ideally would have made new app for the profile section but due to time and small size I am assuming it is fine to keep this project to single app
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    #Cascade will get rid of record on User deletion
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #Don't need to add email here, can derive from the user
    image = models.ImageField(upload_to='profile_pics', default='default.jpg')
    fav_coin = models.TextField(max_length=4, default="BTC")

    def __str__(self):
        return f'{self.user.username} Profile'
