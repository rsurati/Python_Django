from django.urls import path
from PlayQuiz.views import *
from django.conf.urls import url
app_name = 'PlayQuiz'
urlpatterns=[

url(r'^selectTech/$',selectTech,name='selectTech'),
url(r'^selectQuiz/$',selectQuiz,name='selectQuiz'),
url(r'^playquiz/$',playquiz,name='play'),
url(r'^validateAnswer/$',validateAnswer,name='validateAnswer'),
url(r'^record/$',record,name='record'),
url(r'^delete/$',delete,name='delete'),

]