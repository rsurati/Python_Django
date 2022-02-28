from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class user(models.Model):
	User_Role= models.CharField(max_length=10)
	User_Email=models.EmailField(max_length=100)
	User_Birth_Date=models.DateField()
	User_Password=models.CharField(max_length=10)
	User_Name=models.CharField(max_length=100)
	User_Gender=models.CharField(default="Male",max_length=10)


class tech(models.Model):
	Tech_Name=models.CharField(max_length=25)
	Tech_Adder=models.ForeignKey(user,on_delete=models.CASCADE)

class quiz(models.Model):
	Quiz_Name=models.CharField(max_length=100)
	Quiz_Adder=models.ForeignKey(user,on_delete=models.CASCADE)
	Quiz_Tech=models.ForeignKey(tech,on_delete=models.CASCADE)


class question(models.Model):
	Question_Question=models.CharField(max_length=500)
	Question_Option_1=models.CharField(max_length=100)
	Question_Option_2=models.CharField(max_length=100)
	Question_Option_3=models.CharField(max_length=100)
	Question_Option_4=models.CharField(max_length=100)
	Question_Answer=models.CharField(max_length=100)
	Question_Quiz=models.ForeignKey(quiz,on_delete=models.CASCADE)

class ManageScore(models.Model):
	User_id=models.ForeignKey(user,on_delete=models.CASCADE)
	Score=models.CharField(max_length=3)
	Quiz_id=models.ForeignKey(quiz,on_delete=models.CASCADE)
	Play_date=models.CharField(max_length=10)