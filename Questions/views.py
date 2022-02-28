from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
from techquiz.models import user,tech,quiz,question
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required

def managequest(request):
	if request.session.has_key("uid") & request.session.has_key("urole"):
		if request.session['urole']=='admin':	
			qid=request.GET.get("quizid")
			print(qid)
			q=question.objects.filter(Question_Quiz_id=qid);
			qe={'question':q,'qid':qid}
			return render(request,"manageQuestion.html",qe)
	return redirect("login:login")


def addquest(request):
	
	if request.session.has_key("uid") & request.session.has_key("urole"):
		if request.session['urole']=='admin':
				qid=request.GET.get("qid");
				print(qid)
				c={}
				c.update(csrf(request))
				
				return render(request,'addQuestion.html',{'qid':qid})
		return redirect("login:login")

def addQuestDetail(request):
	if request.session.has_key("uid") & request.session.has_key("urole"):	
		if request.session['urole']=='admin':	
			qname=request.POST.get('qname','')
			op1=request.POST.get('op1','')
			op2=request.POST.get('op2','')
			op3=request.POST.get('op3','')
			op4=request.POST.get('op4','')
			answer=request.POST.get('answer','')
			qid=request.POST.get('qid','')
			print(qid)
			
			que=question(Question_Question=qname,Question_Option_1=op1,Question_Option_2=op2,Question_Option_3=op3,Question_Option_4=op4,Question_Answer=answer,Question_Quiz_id=qid)
			que.save()
			return redirect("tech:manage")
	return redirect("login:login")
	
def update(request):
	if request.session.has_key("uid") & request.session.has_key("urole"):
		questid=request.GET['quesid']
		print(questid)
		q=question.objects.filter(id=questid)
		us={'quest':q}
		return render(request,'updateQuestion.html',us)
	return redirect("login:login")

def updateqestinfo(request):
	if request.session.has_key("uid") & request.session.has_key("urole"):
		qname=request.POST.get('qname','')
		op1=request.POST.get('op1','')
		op2=request.POST.get('op2','')
		op3=request.POST.get('op3','')
		op4=request.POST.get('op4','')
		answer=request.POST.get('answer','')
		qeid=request.POST.get('qeid')
		question.objects.filter(id = qeid).update(Question_Question=qname,Question_Option_1=op1,Question_Option_2=op2,Question_Option_3=op3,Question_Option_4=op4,Question_Answer=answer)
		return redirect('tech:manage')
 

	return redirect("login:login")


def delete(request):
	if request.session.has_key("uid") & request.session.has_key("urole"):
		qeid=request.GET['quesid']
		u = question.objects.filter(id = qeid)
		for us in u:
			us.delete()
			return redirect('tech:manage')
	return HttpResponse("hello")

