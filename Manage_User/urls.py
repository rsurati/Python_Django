from django.urls import path
from Manage_User.views import manage,update,delete,updateinfo,add,addUser
from django.conf.urls import url
app_name = 'Manage_User'
urlpatterns=[

url(r'^manage/$',manage,name='manage'),
url(r'^update/$',update,name='update'),
url(r'^delete/$',delete,name='delete'),
url(r'^add/$',add,name='add'),
url(r'^addUser/$',addUser,name='addUser'),
url(r'^updateinfo/$',updateinfo,name='updateinfo'),

]