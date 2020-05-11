from __future__ import absolute_import, unicode_literals
from celery import task 
from celery import shared_task 
from celery import Celery
from celery.schedules import crontab
from datetime import timedelta
from .models import Reminder,Expense
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib import messages
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

celery = Celery(__name__)
celery.config_from_object(__name__)



@shared_task
def send_emailcelery():
	today = date.today()
	toEmailUsers = Reminder.objects.filter(reminder_date=today,reminder_email=True)
	
	for item in toEmailUsers:


		subject = "You have reminder: " + str(item.reminder_type) + " for " +  str(item.reminder_cat.cat_name)
		email_from = settings.EMAIL_HOST_USER
		email_toA = str(item.owner.email)
		email_to = [email_from, email_toA]
		smessage = 'reminder'
		message=EmailMultiAlternatives(subject=subject,body=smessage,from_email=email_from,to=email_to)
		html_template = get_template("core/reminderemail.html").render()
		message.attach_alternative(html_template, "text/html")
		message.send()



@shared_task
def repeat_reminder():
	today = date.today()
	tommorow = today + timedelta(days = 1) 
	nextweek = today + timedelta(days = 7)
	nextmonth = today + relativedelta(months=3)
	nextyear = today + relativedelta(years=1)

	repeatDaily = Reminder.objects.filter(reminder_date=today,reminder_repeat='Daily')
	repeatDaily.update(reminder_date=tommorow)

	repeatWeekly = Reminder.objects.filter(reminder_date=today,reminder_repeat='Weekly')
	repeatWeekly.update(reminder_date=nextweek)

	repeatMonthly = Reminder.objects.filter(reminder_date=today,reminder_repeat='Monthly')
	repeatMonthly.update(reminder_date=nextmonth)

	repeatYearly = Reminder.objects.filter(reminder_date=today,reminder_repeat='Yearly')
	repeatYearly.update(reminder_date=nextyear)


@shared_task
def repeat_expense():
	today = date.today()
	tommorow = today + timedelta(days = 1) 
	nextweek = today + timedelta(days = 7)
	nextmonth = today + relativedelta(months=3)
	nextyear = today + relativedelta(years=1)

	repeatDaily = Expense.objects.filter(expense_date=today,expense_repeat='Daily')	
	repeatDaily.pk = None
	repeatDaily.update(expense_date=tommorow)
	for object in repeatDaily:
 		repeatDaily.save()

	repeatWeekly = Expense.objects.filter(expense_date=today,expense_repeat='Weekly')
	repeatDaily.pk = None
	repeatWeekly.update(expense_date=nextweek)
	for object in repeatWeekly:
		repeatWeekly.save()

	repeatMonthly = Expense.objects.filter(expense_date=today,expense_repeat='Monthly')
	repeatDaily.pk = None
	repeatMonthly.update(expense_date=nextmonth)
	for object in repeatMonthly:
	 	repeatMonthly.save()

	repeatYearly = Expense.objects.filter(expense_date=today,expense_repeat='Yearly')
	repeatDaily.pk = None
	repeatYearly.update(expense_date=nextyear)
	for object in repeatYearly:
	 	repeatYearly.save()





	# subject = 'You have a reminder!'
	# email_from = settings.EMAIL_HOST_USER
	# email_toA = 'xociwi7780@zaelmo.com'
	# email_to = [email_from, email_toA]
	# smessage = 'reminder'
	# message=EmailMultiAlternatives(subject=subject,body=smessage,from_email=email_from,to=email_to)
	# html_template = get_template("core/reminderemail.html").render()
	# message.attach_alternative(html_template, "text/html")
	# message.send()



CELERY_BEAT_SCHEDULE = {
           'every-day-email': {
        'task': 'tasks.send_emailcelery',
        'schedule': crontab(),
        },
         'every-day-repeat-reminder': {
        'task': 'tasks.repeat_reminder',
        'schedule': crontab(),
        },
         'every-day-repeat-expense': {
        'task': 'tasks.repeat_expense',
        'schedule': crontab(),
        }
}