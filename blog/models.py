from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(default='', max_length=50)
    author = models.CharField(default='', max_length=30)
    content = models.TextField()
    views = models.IntegerField(default=0)
    slug = models.CharField(default='', max_length=80)
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + ' by ' + self.author


class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True)
    timeStamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[:13] + "..." + "by " + self.user.username
