from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.
class IpModel(models.Model):
    ip = models.CharField(max_length=100)
    def __str__(self):
        return self.ip

class Post(models.Model):
    pid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    text = RichTextField(max_length=10000)
    thumbnail = models.ImageField(upload_to="",null=True,blank=True)
    thumbnail_url = models.CharField(max_length=500,default=None,null=True,blank=True)
    likes = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    text = models.TextField(max_length=300)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username