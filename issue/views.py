from email import message
from django.shortcuts import render,redirect
from .models import Student,issue
from django.contrib import messages
import uuid
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')

def check(request):
    if request.method=='POST':
        name=request.POST['name']    
        email=request.POST['email']    
        hostel=request.POST['hostel']
        floor=request.POST['floor']
        room=request.POST['room']  
        name=name.upper() 
        password = request.POST['password']
        username = request.POST['username']
           
                    
          
        if Student.objects.filter(usernm=username).exists():
            messages.info(request,"You are already registered , please login.")
            return redirect('/signup')
        else:
            auth_token = str(uuid.uuid4())
            profile=Student.objects.create(name=name,floor=floor,room=room,hostelname=hostel,pwd=password,usernm = username ,auth_token= auth_token,em=email)
            profile.save()
            user_obj = User(username = username , email = email)
            user_obj.set_password(password)
            user_obj.save()
            messages.info(request,"Account successfully created. ")
            return redirect('/signup')
    else:        
        return render(request,'signup.html')
def checklogin(request):
    password = request.POST.get('password')
    username = request.POST.get('username')
    if Student.objects.filter(usernm=username).exists():
    
        us=Student.objects.get(usernm=username)
        uem=us.em
        pss=us.pwd
        if(pss==password):
            return redirect(username+'/profile')
        else:
            messages.info(request,'Incorrect password')
            return redirect('/login')
    else:
        messages.info(request,'Incorrect username/username not registered')
        return redirect('/login')
    
def profile(request,name):
    u=Student.objects.get(usernm=name)
    username=u.usernm
    room=u.room
    floor=u.floor
    email=u.em
    hostel=u.hostelname
    time=u.created_at
    mobile=u.mobno

    return render(request,"profile.html",{'time':time,'name':name,'username':username,'room':room,'floor':floor,'hostel':hostel,'mobile':mobile,'email':email})
def issue(request,name):
    return render(request,"issues.html",{'name':name})
def uissue(request,name):
    return render(request,"uissues.html",{'name':name})
def warden(request):
    return render(request,"warden.html")
def wardencomplains(request):
    return render(request,"complains.html")
def recentissue(request):
    return render(request,"recentissue.html")