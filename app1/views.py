from django.shortcuts import render,redirect,get_list_or_404
from django.contrib.auth import logout,authenticate
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from .models import Post,Comment
from hitcount.views import HitCountDetailView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import CreateView,UpdateView
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.core.files.storage import FileSystemStorage

class SuperUserCheck(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser
# Create your views here.
def index(request):
    return render(request,"index.html")
def usersignup(request):
    if request.method == "POST": 
        username = request.POST["username"]        
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request,"This username is already taken!")
                return redirect("usersignup")        
            else:
                user = User.objects.create_user(username = username,password = password)
                user.save()
                auth_login(request,user)
                return redirect("userblogs")
        else:
            messages.info(request,"The passwords entered are not same!")
            return redirect("usersignup") 
    return render(request,'user_signup.html')
def adminlogin(request):
    if request.method == "POST":         
        username = request.POST.get("username")
        password = request.POST.get("password")               
        user = authenticate(username = username,password = password)  
        # print(user)      
        if user is not None:
            auth_login(request,user)
            return redirect("adminblogs")
        else:
            messages.info(request,"Admin User credentails are incorrect!")
            return redirect("adminlogin")
    return render(request,'login_admin.html')
def userlogin(request):
    if request.method == "POST":         
        username = request.POST.get("username")
        password = request.POST.get("password")               
        user = authenticate(username = username,password = password)  
        # print(user)      
        if user is not None:
            auth_login(request,user)
            return redirect("userblogs")
        else:
            messages.info(request,"Customer User credentails are incorrect!")
            return redirect("userlogin")    
    return render(request,'login_user.html')

@login_required
def temp_dashboard(request):
    user = request.user
    return redirect("")

@login_required
def dashboard(request,user = None):    
    return render(request,"dashboard.html")
    
@user_passes_test(lambda u: u.is_superuser)
def blogs(request):
    user = request.user
    posts = Post.objects.all()
    return render(request,'blogs.html',{"user":user,'posts':posts})

@login_required
def userblogs(request):
    user = request.user
    posts = Post.objects.all()
    return render(request,'blogs.html',{"user":user,'posts':posts})


# @login_required
# def blog(request,pid):
#     post = Post.objects.filter(pid = pid)
#     post = post[0]
#     # print(post)

#     return render(request,'blog.html',{"i":post})
# @login_required
class blog(HitCountDetailView,LoginRequiredMixin,View): 
    model1 = Post  
    model2 = Comment
    template =  'blog.html'
    count_hit = True

    def get(self,request,pid):
        post = self.model1.objects.filter(pid = pid)
        post = post[0]
        comments = self.model2.objects.filter(post = post)
        # print(comments)
        # print(comments)
        counts = comments.count()
        # likes = self.model1.likescount(post)
        # print(likes)
        # print(counts)
        return render(request,self.template,{"i":post,'comments':comments,'count':counts})
    
    def post(self,request,pid):
        post = self.model1.objects.filter(pid = pid)
        post = post[0]
        user = request.user
        text = request.POST.get("comment")
        post_ins = post
        ins = Comment(user=user,text=text,post=post_ins)
        ins.save()        
        comments = self.model2.objects.filter(post = post)
        # print(comments)
        counts = comments.count()
        return render(request,self.template,{"i":post,'comments':comments,"count":counts})
         
# def addblog(request):
#     return render(request,"addblog.html")
# name = ''
class addblog(SuperUserCheck,CreateView):
    model = Post
    template = "addblog.html"
    fields = "__all__"    

    def get(self,request):
        # form = self.form()
        
        form = PostForm()
        return render(request,self.template,{"form":form})
    
    def post(self,request):
        form = PostForm(request.POST)
        # print(form)
        if form.is_valid():
            # print("hi")
            # print(form)
            # global name
            # name=''
            # docu = request.FILES['thumbnail']
            # fs = FileSystemStorage()
            # file = fs.save(docu.name, docu)
            p = form.save() 
            # f = request.FILES["id_thumbnail"]
            # print(request.POST.get("id_thumbnail"))
            # print(request.POST.get("title"))
        else:
            print(form.errors.as_data())    
        return redirect("adminblogs")
        
# class editblog(UpdateView):
#     def get(self,request,pid):
#         post = Post.objects.filter(pid = pid)
#         post = post[0]
#         form = PostForm(request.GET,instance=post)
#         return render(request,'editblog.html',{'form':form})
@user_passes_test(lambda u: u.is_superuser)
def editblog(request,pid):
    if request.method != 'POST':
        post = Post.objects.filter(pid = pid)
        post = post[0]
        form = PostForm(instance=post)
        return render(request,'editblog.html',{'form':form})
    else:
        post = Post.objects.filter(pid = pid)
        post = post[0]
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog',args = [str(pid)]))

class deleteblog(SuperUserCheck,View):
    def get(self,request,pid):
        post = Post.objects.filter(pid = pid)
        post = post[0]
        post.delete()
        return redirect('adminblogs')


def likes(request,pid):
    post = Post.objects.filter(pid = pid)
    post = post[0]
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('blog',args=[str(pid)]))
    # return render(request,"addblog.html")



@login_required
def userlogout(request):
    logout(request)
    return redirect("index")
    
