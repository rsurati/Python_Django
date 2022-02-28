from django.urls import path
from techquiz.views import home,addquiz,addquizdetatil,login,manage,update,updateinfo,delete
from django.conf.urls import url
app_name = 'techquiz'
urlpatterns=[
url(r'^Login/$',login,name='login'),
url(r'^Home/$',home,name='home'),
url(r'^Addquiz/$',addquiz,name='addquiz'),
url(r'^Addquizdetails',addquizdetatil,name='addquizdetatil'),
url(r'^manage/$',manage,name='manage'),
url(r'^update/$',update,name='update'),
url(r'^updateinfo/$',updateinfo,name='updateinfo'),
url(r'^delete/$',delete,name='delete'),





]