from django.urls import path
from Questions.views import managequest,addquest,addQuestDetail,updateqestinfo,update,delete
from django.conf.urls import url
app_name = 'Questions'
urlpatterns=[

url(r'^manage/$',managequest,name='manage'),
url(r'^addquest/$',addquest,name='addquest'),
url(r'^addQuestDetail/$',addQuestDetail,name='addQuestDetail'),
url(r'^updateqestinfo/$',updateqestinfo,name='updateqestinfo'),
url(r'^update/$',update,name='update'),
url(r'^delete/$',delete,name='delete'),



]