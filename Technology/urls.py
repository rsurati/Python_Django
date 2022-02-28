from django.urls import path
from Technology.views import manage,add,addTech,update,delete,updateinfo
from django.conf.urls import url
app_name = 'Technology'
urlpatterns=[

url(r'^manage/$',manage,name='manage'),
url(r'^add/$',add,name='add'),
url(r'^addTech/$',addTech,name='addTech'),
url(r'^update/$',update,name='update'),
url(r'^delete/$',delete,name='delete'),
url(r'^updateinfo/$',updateinfo,name='updateinfo'),

]