from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from techquiz.models import user
from django.contrib import auth
from django.template.context_processors import csrf
from django.views import generic
from django.core.mail import send_mail

def login(request):
	c={}
	c.update(csrf(request))
	return render_to_response('login.html',c)

def register(request):
	c1={}
	c1.update(csrf(request))
	return render_to_response('Register.html',c1)

def addUser(request):
	
	Uname=request.POST.get('user','')
	passw=request.POST.get('password','')
	email=request.POST.get('Email','')
	bdate=request.POST.get('BDate','')
	gender=request.POST.get('gender','')

	u= user(User_Role="user",User_Email=email,User_Birth_Date=bdate,User_Password=passw,User_Gender=gender,User_Name=Uname)
	u.save()
	return redirect('login:login')


def homepage(request):
	return render_to_response('Homepage.html')


def forgot(request):
	c2={}
	c2.update(csrf(request))
	return render_to_response('forgot.html',c2)

def forgotdetail(request):
	us=request.POST.get('user','')
	email=request.POST.get('email','')

	u=user.objects.filter(User_Name=us,User_Email=email)
	if u.exists():
		
	
		fu=user.objects.get(User_Name=us,User_Email=email)
		content="your new password is :="+str(fu.User_Password)
		send_mail('Hello '+str(fu.User_Name),content,'ramsky2021@gmail.com',[fu.User_Email],fail_silently=True)
	return redirect('login:login')

