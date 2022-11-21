from django.contrib import admin
from .models import Post,IpModel,Comment
# Register your models here.
admin.site.register(Post)
admin.site.register(IpModel)
admin.site.register(Comment)