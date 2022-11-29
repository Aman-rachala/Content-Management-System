from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [    
    path('',views.index,name = 'index'),
    
    
    path("dashboard",views.dashboard,name = "dashboard"),
    #ADMIN
    path('auth/admin',views.adminlogin,name = "adminlogin"),
    path("blogs",views.blogs,name = 'adminblogs'),  
    path("blogs/<int:pid>",views.blog.as_view(),name = 'adminblog'),
    path("blogs/create",views.addblog.as_view(),name = "addblog"),
    path("blogs/like/<str:pid>",views.likes,name = "likes"),
    path("blogs/edit/<str:pid>",views.editblog,name = "editblog"),
    path("blogs/delete/<str:pid>",views.deleteblog.as_view(),name = "deleteblog"),
    #USER
    path('signup',views.usersignup,name = "usersignup"),
    path("user/blogs",views.userblogs,name = 'userblogs'),
    path('auth/user',views.userlogin,name = "userlogin"),
    path("user/blogs",views.userblogs,name = 'userblogs'),
    path("user/blogs/<int:pid>",views.blog.as_view(),name = 'blog'),
    # path('blog/<int:pid>', PostDetailView.as_view(), name='blog'),
    path("user/blogs",views.blogs,name = "userblogs"),
    path("logout",views.userlogout,name = "logout"),  
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
]