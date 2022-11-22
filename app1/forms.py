from django.forms import ModelForm
# from django import form
from .models import Comment,Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','text','thumbnail']

