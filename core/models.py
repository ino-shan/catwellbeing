from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.

GENDER_CHOICES =[
	('Male','Male'),
	('Female','Female')
]

REPEAT_CHOICES =[
	('Repeat (Off)','Repeat (Off)'),
	('Daily','Daily'),
	('Weekly','Weekly'),
	('Monthly','Monthly'),
	('Yearly','Yearly'),
]




class Cat(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	cat_name = models.CharField(max_length=128)
	gender = models.CharField(max_length=8,choices=GENDER_CHOICES)
	birthday = models.DateField()
	imagename = models.CharField(max_length=1000,default="none")
	imageurl = models.CharField(max_length=1000,default="none")
	cat_weight = models.FloatField(null=True,blank=True)
	cat_weight_unit = models.CharField(max_length=16)
	cat_breed = models.CharField(max_length=64,null=True,blank=True)
	Spayed_Neutered = models.BooleanField()
	microchip_number = models.CharField(max_length=15,null=True,blank=True)
	insurance_provider = models.CharField(max_length=64,null=True,blank=True)
	insurance_policy_number = models.CharField(max_length=20,null=True,blank=True)
	clinic_name = models.CharField(max_length=64,null=True,blank=True)
	

class Reminder(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	reminder_type = models.CharField(max_length=128)
	reminder_date = models.DateField()
	reminder_cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
	reminder_email = models.BooleanField(default=False)
	reminder_repeat = models.CharField(default="Repeat (Off)",max_length=128,choices=REPEAT_CHOICES)

class MedicalRecord(models.Model):
	cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
	title = models.CharField(max_length=1024)
	description = models.CharField(max_length=2048)
	recordDate = models.DateField(default=datetime.date.today)
	imagename = models.CharField(max_length=1000,default="none")
	imageurl = models.CharField(max_length=1000,default="none")

class Forum(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=1024)
	description = models.CharField(max_length=2048)
	created_at = models.DateField()

class Comment(models.Model):
	forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	description = models.TextField(max_length=1024)
	created_at = models.DateTimeField()

class Veterinary(models.Model):
	name = models.CharField(max_length=1024)
	

class Review(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	vet_clinic = models.ForeignKey(Veterinary, on_delete=models.CASCADE)
	review_rating = models.IntegerField(default=5)
	review_text = models.CharField(max_length=1024)
	

class Expense(models.Model):
	title = models.CharField(max_length=1024)
	cost = models.FloatField()
	expense_date = models.DateField()
	expender = models.ForeignKey(User, on_delete=models.CASCADE)
	expense_repeat = models.CharField(default="Repeat (Off)",max_length=128,choices=REPEAT_CHOICES)




