
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
from techquiz.models import user,tech,quiz,question,ManageScore
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.core.mail import send_mail

def selectTech(request):
	if request.session.has_key("uid"):
		
		techs=tech.objects.all()
		
		us={'tech':techs}
		return render(request,'selectTech.html',us)
	return redirect("login:login")

def selectQuiz(request):
	if request.session.has_key("uid"):
		tid=request.GET.get("techid")
		print(tid)
		q=quiz.objects.filter(Quiz_Tech=tid)
		print(q)
		qd={"quiz":q}
		return render(request,'selectQuiz.html',qd)
	return redirect("login:login")	

def playquiz(request):
	if request.session.has_key("uid"):
		qid=request.GET.get("quizid")
		print(qid)
		qest=question.objects.filter(Question_Quiz_id=qid)
		print(qest)
		c={}
		c.update(csrf(request))
		return render(request,"Question.html",{'quest':qest,'qid':qid})
	return redirect("login:login")	

def validateAnswer(request):
	if request.session.has_key("uid"):
		quizid=request.POST.get("qid")
		print(quizid)
		q=question.objects.filter(Question_Quiz_id=quizid)
		score=0
		flag=0
		for qe in q:
			print(request.POST.get(str(qe.id)))
			if qe.Question_Answer==request.POST.get(str(qe.id)):
				score=score+1

			else:
				pass
		u=user.objects.get(id=int(request.session["uid"]))
		qu=quiz.objects.get(id=quizid)
		m=ManageScore(User_id=u,Score=score,Play_date=str(datetime.date(datetime.now())),Quiz_id=qu)
		m.save();
		qe=question.objects.all();
		content="Your played quiz :-  "+qu.Quiz_Name+ "  and Score of that Quiz is :-"+str(score)
		if(flag==0):
			send_mail('Hello '+str(u.User_Name),
			content,
			'ramsky2021@gmail.com',
			[u.User_Email],
			fail_silently=True)
			flag=1
		else:
			pass
		return render(request,'viewresult.html',{"question":qe,'score':score})
	return redirect("login:login")


def record(request):
	if request.session.has_key("uid"):
		uid=int(request.session['uid'])

		m=ManageScore.objects.filter(User_id=uid)
		md={"score":m}
		
		return render(request,"record.html",md)
	return redirect("login:login")
	
def delete(request):
	if request.session.has_key("uid"):
		qeid=request.GET['msid']
		u = ManageScore.objects.filter(id = qeid)
		for us in u:
			us.delete()
			return redirect('play:record')
	return redirect("login:login")



