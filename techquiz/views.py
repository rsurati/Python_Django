from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
from techquiz.models import user,tech,quiz
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required

def login(request):
		username = request.POST.get('user', '')
		password = request.POST.get('password', '')

		u=user.objects.filter(User_Name=username,User_Password=password)
		if u.exists():
			for o in u:
				request.session['uid']=o.id
				if(o.User_Role=="user"):
					return redirect('play:selectTech')
				
				request.session['urole']=o.User_Role
		else:
			return redirect('login:login')

		return redirect('tech:home')

def manage(request):
	
		if request.session.has_key("uid") & request.session.has_key("urole"):
			if request.session['urole']=='admin':

				te=quiz.objects.all()
			
				t={'quiz':te}
				return render(request,'managequiz.html',t)

		return redirect("login:login")


def home(request):
		return render_to_response('Home.html',{})


def addquiz(request):
	if request.session.has_key("uid") & request.session.has_key("urole"):
		if request.session['urole']=='admin':
				c={}
				c.update(csrf(request))
				t=tech.objects.all()
				td={'tech':t}
				return render(request,'addquiz.html',td)
	return redirect("login:login")

def addquizdetatil(request):
	if request.session.has_key("uid") & request.session.has_key("urole"):
		if request.session['urole']=='admin':
			name=request.POST.get('qname','')
			tid=int(request.POST.get('tech',''))
			t=tech.objects.get(id=tid)
			u=user.objects.get(id=request.session['uid'])
			
			q= quiz(Quiz_Name=name,Quiz_Tech=t,Quiz_Adder=u)
			q.save()
			print("save record")
			return redirect('tech:manage')
	return redirect("login:login")	


def update(request):
	if request.session.has_key("uid") & request.session.has_key("urole"):
		if request.session['urole']=='admin':
			qid=request.GET['qid']
			print(qid)
			q=quiz.objects.filter(id=qid)
			t=tech.objects.all()
			us={'quiz':q,'tech':t}
			return render(request,'update.html',us)
	return redirect("login:login")

def updateinfo(request):
	if request.session.has_key("uid") & request.session.has_key("urole"):
		if request.session['urole']=='admin':
			qid=int(request.POST.get('qid',''))
			qname=request.POST.get('qname','')
			tid=int(request.POST.get('tech',''))
			t=tech.objects.get(id=tid)
			quiz.objects.filter(id = qid).update(Quiz_Tech=t,Quiz_Name=qname)
			return redirect('tech:manage')
	return redirect("login:login")


		

def delete(request):
	if request.session.has_key("uid") & request.session.has_key("urole"):
		if request.session['urole']=='admin':
			qid=request.GET['qid']
			q = quiz.objects.filter(id = qid)
			for o in q:
				o.delete()
				return redirect('tech:manage')
	return redirect("login:login")