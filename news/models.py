from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=120)
    post = models.TextField()
    date = models.DateTimeField()
    adminchecked = models.BooleanField(default=False, null=True)
    gender=models.CharField(max_length=10,default='Не указан')

    def __str__(self):
        return self.title
