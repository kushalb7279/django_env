from django.db import models
from django.contrib.auth.models import User
from PIL import Image    #imported from pillow library

#this is used for profile pics
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  #one to one between profile and user
    image = models.ImageField(default='defult.jpg', upload_to='profile_pics') #creates directory profile_pics

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self,*args, **kwargs):      #this function written to override save method and resize if size of pic is more
    #     super().save(*args, **kwargs)    #wont work in aws s3 bucket, explore lambda later
    #
    #     img = Image.open(self.image.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
