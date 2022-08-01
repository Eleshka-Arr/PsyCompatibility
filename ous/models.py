from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Ous(models.Model):
    post = models.TextField()
    img = models.ImageField(upload_to='images/', blank=True, null=True)
    @property
    def img_url(self):
        if self.img and hasattr(self.img, 'url'):
            return self.img
    def __str__(self):
        return self.post


class Author(models.Model):
    SecondName = models.TextField()
    FirstName = models.TextField()
    img = models.ImageField()
    def __str__(self):
        return self.SecondName +" "+ self.FirstName +" "
