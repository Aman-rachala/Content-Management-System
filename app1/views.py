from django.shortcuts import render,redirect
from django.contrib.auth import logout,authenticate
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
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
                return redirect("blogs")
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
            return redirect("dashboard")
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
    
@login_required
def blogs(request):
    user = request.user
    return render(request,'blogs.html',{"user":user})

@login_required
def userlogout(request):
    logout(request)
    return redirect("index")
    