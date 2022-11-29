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
    title = models.CharField(max_length=50)
    text = RichTextField(max_length=100000)
    thumbnail = models.ImageField(upload_to="media",blank = True,null=True)    
    likes = models.ManyToManyField(User,related_name='blog_post',blank=True)
    date = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.title

    # def likescount(self):
    #     count = 0
    #     for i in self.User.all():
    #         count += 1
    #     return count

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    text = models.TextField(max_length=300)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username