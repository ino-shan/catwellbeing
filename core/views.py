from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Cat, Reminder, MedicalRecord, Forum, Comment, Veterinary, Expense, Review
from django.http import QueryDict
from django.views.decorators.csrf import csrf_exempt
from datetime import date, datetime ,time, timedelta
from django.core.files.storage import FileSystemStorage
from users.models import Profile
from geopy.geocoders import Nominatim
from dateutil.relativedelta import relativedelta

import os
from django.conf import settings


import random
# Create your views here.




@login_required
def home(request):

	user_reminders = Reminder.objects.filter(owner=request.user)
	context = {"user_reminders":user_reminders}
	return render(request, 'core/home.html',context)

@csrf_exempt
def cats(request):
	try:
		if request.method == "POST" and request.FILES['catimage']:
			document = request.FILES['catimage']
			cat_name = request.POST['cat_name_placeholder']
			fs = FileSystemStorage()
			imagename = fs.save(document.name, document)
			
			imageurl = fs.url(imagename)
			
			previous_image = Cat.objects.filter(owner=request.user,cat_name=cat_name)[0].imagename
			
			file_remove = settings.MEDIA_ROOT+"/"+previous_image
			try:
				os.remove(file_remove)
			except:
				pass
			Cat.objects.filter(owner=request.user,cat_name=cat_name).update(imagename=imagename,imageurl=imageurl)
	except:
		pass

	try:
		if request.method == "POST" and request.FILES['recordimage']:
			document = request.FILES['recordimage']
		
			record_id = request.POST['record_id_up']
			fs = FileSystemStorage()
			imagename = fs.save(document.name, document)			
			imageurl = fs.url(imagename)
			
			previous_image = MedicalRecord.objects.filter(pk=int(record_id))[0].imagename
		
			file_remove = settings.MEDIA_ROOT+"/"+previous_image
			try:
				os.remove(file_remove)
			except:
				pass
			MedicalRecord.objects.filter(pk=int(record_id)).update(imagename=imagename,imageurl=imageurl)
			
	except:
		pass


	try:
		if request.method == 'POST' and request.POST['objective']=="CREATE_CAT":
			cat_name = request.POST['cat_name']
			gender = request.POST['gender']
			birthday = request.POST['birthday']
			cat_weight = request.POST['cat_weight']
			cat_weight_unit = request.POST['cat_weight_unit']
			cat_breed = request.POST['cat_breed']
			Spayed_Neutered = request.POST['Spayed_Neutered']
			microchip_number = request.POST['microchip_number']
			insurance_provider = request.POST['insurance_provider']
			insurance_policy_number = request.POST['insurance_policy_number']
			clinic_name = request.POST['clinic_name']


			
			

			if Spayed_Neutered == 'Yes':		
				spayed = True
			elif Spayed_Neutered == 'No':			
				spayed = False	
			
			
			Cat.objects.create(owner=request.user,cat_name=cat_name,gender=gender, birthday=birthday,
		    cat_weight=cat_weight,cat_weight_unit=cat_weight_unit,
			cat_breed=cat_breed,Spayed_Neutered=spayed,
			microchip_number=microchip_number,insurance_provider=insurance_provider,
			insurance_policy_number=insurance_policy_number,clinic_name=clinic_name,imagename="",imageurl="")
	except:
		pass

	try:

		if request.method == "PUT" and  QueryDict(request.body).get('objective')=="EDIT_CAT":
			PUT =  QueryDict(request.body)
			cat_name = PUT.get('cat_name')
			gender = PUT.get('gender')
			birthday = PUT.get('birthday')
			cat_photo = PUT.get('cat_photo')
			cat_weight = PUT.get('cat_weight')
			cat_weight_unit = PUT.get('cat_weight_unit')
			cat_breed = PUT.get('cat_breed')
			Spayed_Neutered = PUT.get('Spayed_Neutered')
			microchip_number = PUT.get('microchip_number')
			insurance_provider = PUT.get('insurance_provider')
			insurance_policy_number = PUT.get('insurance_policy_number')
			clinic_name = PUT.get('clinic_name')


			if Spayed_Neutered == 'Yes' :		
				spayed = True
			elif Spayed_Neutered == 'No':			
				spayed = False

			if cat_weight is '' :		
				cat_weight = None
			
				

			if birthday == '':
				Cat.objects.filter(owner=request.user,cat_name=cat_name).update(gender=gender,
			    cat_weight=cat_weight,cat_weight_unit=cat_weight_unit,
				cat_breed=cat_breed,Spayed_Neutered=spayed,
				microchip_number=microchip_number,insurance_provider=insurance_provider,
				insurance_policy_number=insurance_policy_number,clinic_name=clinic_name)
			else:
				Cat.objects.filter(owner=request.user,cat_name=cat_name).update(gender=gender,birthday=birthday,
			    cat_weight=cat_weight,cat_weight_unit=cat_weight_unit,
				cat_breed=cat_breed,Spayed_Neutered=spayed,
				microchip_number=microchip_number,insurance_provider=insurance_provider,
				insurance_policy_number=insurance_policy_number,clinic_name=clinic_name)
	except:
		pass
		
	try:
		if request.method == "PUT" and  QueryDict(request.body).get('objective')=="DELETE_CAT":
			cat_name =  QueryDict(request.body).get('cat_name')
			Cat.objects.get(owner=request.user,cat_name=cat_name).delete()
	except:
		pass

	try:
		if request.method == 'POST' and request.POST['objective']=="CREATE_MEDICAL_RECORD":
			cat_model = request.POST['cat_model']
			title = request.POST['title']
			description = request.POST['description']
			the_cat = Cat.objects.get(owner=request.user,cat_name=cat_model)
			MedicalRecord.objects.create(cat=the_cat,title=title,description=description,imagename="",imageurl="")
	except:
		pass

	try:
		if request.method == "PUT" and QueryDict(request.body).get('objective') == "DELETE_MEDICAL_RECORD":
			record_id =  QueryDict(request.body).get('record_id')
			MedicalRecord.objects.get(pk=record_id).delete()
	except:
		pass

	try:
		if request.method == "PUT" and QueryDict(request.body).get('objective') == "CHANGE_MEDICAL_RECORD":
			PUT =  QueryDict(request.body)
			record_id = PUT.get('record_id_change')
			new_title = PUT.get('title_change')
			new_description = PUT.get('description_change')
			MedicalRecord.objects.filter(pk=int(record_id)).update(title=new_title,description=new_description)
	except:
		pass

	
	user_cats = Cat.objects.filter(owner=request.user)
	cat_medical_records = MedicalRecord.objects.filter(cat__owner=request.user)
	context = {"owner_cats":user_cats,"cat_medical_records":cat_medical_records}
	return render(request, 'core/cats.html',context)

@csrf_exempt
def reminders(request):
	if request.method == 'POST':
		reminder_type = request.POST['reminder_for']
		reminder_date = request.POST['reminder_date']
		reminder_cat = request.POST['reminder_who']
		reminder_email = request.POST['reminder_email']
		reminder_repeat = request.POST['reminder_repeat']
		the_cat = Cat.objects.get(owner=request.user,cat_name=reminder_cat)

		if reminder_email == 'true':
			reminderBool = True
		else:
			reminderBool = False

		
			
		Reminder.objects.create(owner=request.user,reminder_type=reminder_type,reminder_date=reminder_date,reminder_cat=the_cat,reminder_email=reminderBool,reminder_repeat=reminder_repeat)

	if request.method == "PUT" and QueryDict(request.body).get('objective') == "DELETE_REMINDER":
		reminder_id =  QueryDict(request.body).get('reminder_id')
		Reminder.objects.get(pk=reminder_id).delete()

		




	user_cats = Cat.objects.filter(owner=request.user)
	user_reminders = Reminder.objects.filter(owner=request.user)
	context = {"owner_cats":user_cats,"user_reminders":user_reminders}
	return render(request, 'core/reminders.html',context)


def findvet(request):
	if request.method == 'POST' and request.POST['objective']=="GET_LAT_LONG":
		geolocator = Nominatim(user_agent="cat_Wellbeing")
		userText = request.POST['inputtedText']
		location = geolocator.geocode(userText)
		if location!=None :
			adr = location.address
			userlat = str(location.latitude)
			userlng = str(location.longitude)
			userloc = userlat + ',' + userlng

			return HttpResponse(userloc)
		else:
			return HttpResponse("Can't find Location")

	if request.method == 'POST' and request.POST['objective']=="CREATE_VET":
		name = request.POST['name']
		Veterinary.objects.create(name=name)



	if request.method == 'POST' and request.POST['objective']=="CREATE_REVIEW":
		reviewText = request.POST['review']
		reviewRating = request.POST['rating']
		reviewVet = request.POST['vet']
		theVet = Veterinary.objects.get(name=reviewVet)
		Review.objects.create(owner=request.user,vet_clinic=theVet,review_rating=reviewRating,review_text=reviewText)

	
	user_reviews = Review.objects.filter(owner=request.user)
	all_reviews = Review.objects.all()
	all_vets = Veterinary.objects.all()
	context = {"all_vets": all_vets,"user_reviews":user_reviews,"all_reviews":all_reviews}
	#return render(request, 'core/findvet.html', context)
	
	return render(request, 'core/findvet.html', context)



def forum(request):
	if request.method == "POST" and request.POST['objective'] == "CREATE_FORUM":
		forum_title = request.POST['forum_title']
		forum_description = request.POST['forum_description']
		Forum.objects.create(owner=request.user,title=forum_title,description=forum_description,created_at=date.today())

	all_forums = Forum.objects.all()
	context = {"all_forums": all_forums}
	return render(request, 'core/forum.html', context)

def forumpage(request,id):
	this_forum = Forum.objects.get(pk=id)
	if request.method == "POST" and request.POST['objective'] == "CREATE_FORUM_RESPONSE":
		response_description = request.POST['response_description']
		created_at = datetime.now()
		Comment.objects.create(forum=this_forum,owner=request.user,description=response_description,created_at=created_at)
	this_forum_responses = Comment.objects.filter(forum=this_forum)
	user_profile = Profile.objects.all()
	context = {"this_forum": this_forum, "this_forum_responses": this_forum_responses, "user_profile":user_profile}
	return render(request, 'core/forumpage.html', context)

def expenses(request):
	list_of_cat_expenses = ["Bed", "Microchip", "Vaccinations", "Neutering", "Scratching Post",
	"Toys", "Health Check", "Flea and Worming Treatment", "Pet Insurance", "Cat Food", "Litter", "Other"]






	if request.method == "POST" and request.POST['objective'] == "CREATE_EXPENSE":
		expense_title = request.POST['expense_title']
		expense_value = request.POST['expense_value']
		expense_date = request.POST['expense_date']
		expense_repeat = request.POST['expense_repeat']
		Expense.objects.create(title=expense_title,cost=expense_value,expense_date=expense_date,expender=request.user,expense_repeat=expense_repeat)

	user_expenses = Expense.objects.filter(expender=request.user)
	user_cats = Cat.objects.filter(owner=request.user)
	context = {"owner_cats":user_cats, "list_of_cat_expenses":list_of_cat_expenses,"user_expenses":user_expenses}
	return render(request, 'core/expenses.html', context)

def expensedetailpage(request,expense):
	expense = " ".join(expense.split("-"))
	report = Expense.objects.filter(expender=request.user,title=expense)
	context = {"report": report}
	return render(request, 'core/expensedetailpage.html', context)