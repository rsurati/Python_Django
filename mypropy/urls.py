from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.homepage,name='main'),
    url(r'^Login_Module/',include('Login_Module.urls',namespace='login')),
    url(r'^techquiz/',include('techquiz.urls',namespace='tech')),
    url(r'^Manage_User/',include('Manage_User.urls',namespace='user')),
    url(r'^Technology/',include('Technology.urls',namespace='technology')),
    url(r'^Questions/',include('Questions.urls',namespace='ques')),
    url(r'^PlayQuiz/',include('PlayQuiz.urls',namespace='play')),
]
