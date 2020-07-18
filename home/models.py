from django.db import models


# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(default='', max_length=50)
    email = models.CharField(default='', max_length=50)
    phone = models.CharField(default='', max_length=13)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from' + " " + self.name
