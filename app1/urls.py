from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [    
    path('',views.index,name = 'index'),
    path('signup',views.usersignup,name = "usersignup"),
    path('auth/admin',views.adminlogin,name = "adminlogin"),
    path('auth/user',views.userlogin,name = "userlogin"),
    path("dashboard",views.dashboard,name = "dashboard"),
    path("blogs",views.blogs,name = 'adminblogs'),  
    path("blog/<int:pid>",views.blog.as_view(),name = 'blog'),
    # path('blog/<int:pid>', PostDetailView.as_view(), name='blog'),
    path("user/blogs",views.blogs,name = "userblogs"),
    path("logout",views.userlogout,name = "logout"),  
     path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
]