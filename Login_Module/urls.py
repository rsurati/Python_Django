from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as authviews
app_name = 'Login_Module'
urlpatterns=[
url(r'^$',views.homepage,name='homepage'),
url(r'^Login/$',views.login,name='login'),
url(r'^Register/$',views.register,name='register'),
url(r'^addUser/$',views.addUser,name='add'),
url(r'^forgot/$',views.forgot,name='forgot'),
url(r'^forgotdetail/$',views.forgotdetail,name='forgotdetail'),
url(r'^logout/$',authviews.LogoutView.as_view(),{'next_page':'login:login'},name='logout'),
]