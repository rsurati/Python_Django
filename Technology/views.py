
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
from techquiz.models import tech
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required

def manage(request):
	if request.session.has_key("uid") & request.session.has_key("urole"):
		if request.session['urole']=='admin':
			tec=tech.objects.all()		
			te={'techs':tec}
			return render(request,'managetech.html',te)
	return redirect("login:login")

def add(request):
	if request.session.has_key("uid") & request.session.has_key("urole"):
		if request.session['urole']=='admin':
			c1={}
			c1.update(csrf(request))
			return render_to_response('addTech.html',c1)
		return redirect("login:login")

def addTech(request):
	if request.session.has_key("uid") & request.session.has_key("urole"):
		if request.session['urole']=='admin':
			tname=request.POST.get('tech_name','')
			aid=request.session["uid"]
			t= tech(Tech_Name=tname,Tech_Adder_id=aid)
			t.save()
			print("save record")
			return redirect('technology:manage')
	return redirect("login:login")


def update(request):
	if request.session.has_key("uid") & request.session.has_key("urole"):
		if request.session['urole']=='admin':
			tid=request.GET['techid']
			print(tid)
			t=tech.objects.filter(id=tid)
			te={'tech':t}
			return render(request,'updatetech.html',te)
	return redirect("login:login")

def updateinfo(request):
	if request.session.has_key("uid") & request.session.has_key("urole"):	
		if request.session['urole']=='admin':
			tname=request.POST.get('tech_name','')
			tid=request.POST.get('tid','')
			tech.objects.filter(id = tid).update(Tech_Name = tname)
			return redirect('technology:manage')
	return redirect("login:login") 


def delete(request):
	if request.session.has_key("uid") & request.session.has_key("urole"):
		if request.session['urole']=='admin':
			tid=request.GET['techid']
			te = tech.objects.filter(id = tid)
			for  t in te:
				t.delete()
				return redirect('technology:manage')
	return redirect("login:login")


