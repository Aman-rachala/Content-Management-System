from django.forms import ModelForm,widgets
from django import forms
from .models import Comment,Post

class PostForm(ModelForm):
    # title = forms.CharField(widget = forms.TextInput(attrs = {
    #     "class":"",
    #     "type": "",
    #     "placeholder":""
    # }),label = "")
    # text = forms.TextField(widget = forms.Textarea(attrs = {
    #     "class":"",
    #     "type": "",
    #     "placeholder":""
    # }),label = "")
    # thumbnail = forms.ImageField(widget = forms.TextInput(attrs = {
    #     "class":"",
    #     "type": "",
    #     "placeholder":""
    # }),label = "")
    class Meta:
        model = Post
        fields = ['title','text','thumbnail']
        # widget = {
        #     'title' : form.TextInput(attrs={'class':"form-control"})
        # }
        

