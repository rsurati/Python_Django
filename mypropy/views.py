from django.shortcuts import redirect,render

def homepage(request):
	return render(request,'Homepage.html',{})