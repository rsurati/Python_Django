
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
from techquiz.models import user
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required

def manage(request):
	if request.session.has_key("uid") & request.session.has_key("urole"):
		
		users=user.objects.all()
		
		us={'users':users}
		return render(request,'manage.html',us)
	return redirect("login:login")

def update(request):
	if request.session.has_key("uid") & request.session.has_key("urole"):
		usid=request.GET['userid']
		print(usid)
		u=user.objects.filter(id=usid)
		us={'user':u}
		return render(request,'updateuser.html',us)
	return redirect("login:login")

def updateinfo(request):
	if request.session.has_key("uid") & request.session.has_key("urole"):
		uid=request.POST.get('id','')
		Uname=request.POST.get('user','')
		passw=request.POST.get('password','')
		email=request.POST.get('Email','')
		bdate=request.POST.get('BDate','')
		role=request.POST.get('role','')
		user.objects.filter(id = uid).update(User_Name = Uname, User_Birth_Date = bdate,User_Email=email,User_Password=passw,User_Role=role)
		return redirect('user:manage')
 

	return redirect("login:login")

def delete(request):
	if request.session.has_key("uid") & request.session.has_key("urole"):
		usid=request.GET['userid']
		u = user.objects.filter(id = usid)
		for us in u:
			u.delete()
			return redirect('user:manage')
	return redirect("login:login")


def add(request):
	c1={}
	c1.update(csrf(request))
	return render_to_response('addUser.html',c1)

def addUser(request):

	if request.session.has_key("uid") & request.session.has_key("urole"):
		Uname=request.POST.get('user','')
		passw=request.POST.get('password','')
		email=request.POST.get('Email','')
		bdate=request.POST.get('BDate','')
		gender=request.POST.get('gender','')

		u= user(User_Role="user",User_Email=email,User_Birth_Date=bdate,User_Password=passw,User_Gender=gender,User_Name=Uname)
		u.save()
		print("save record")
		return redirect('user:manage')
	return redirect("login:login")