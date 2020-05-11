from django.test import TestCase, Client
from django.urls import reverse, resolve
from core.views import *

class UrlTest(TestCase):
	def setUp(self):
		self.client = Client()

	def test_home(self):
		# path('', views.home, name='core-home'),
		url = reverse('core-home')
		self.assertEqual(resolve(url).func, home)
		self.assertEqual(resolve(url).url_name, "core-home")
		response = self.client.get(reverse('core-home'))
		self.assertEqual(response.status_code, 302)

	def test_cats(self):
		# path('cats/', views.cats, name='core-cats'),
		url = reverse('core-cats')
		self.assertEqual(resolve(url).func, cats)
		self.assertEqual(resolve(url).url_name, "core-cats")

		# response = self.client.get(reverse('core-cats'))
		# self.assertEqual(response.status_code, 200)
		# self.assertTemplateUsed(response, 'core/cats.html')

	def test_reminders(self):
		# path('reminders/', views.reminders, name='core-reminders'),
		url = reverse('core-reminders')
		self.assertEqual(resolve(url).func, reminders)
		self.assertEqual(resolve(url).url_name, "core-reminders")

		# response = self.client.get(reverse('core-reminders'))
		# self.assertEqual(response.status_code, 200)
		# self.assertTemplateUsed(response, 'core/reminders.html')


	def test_forum(self):
		# path('forum/', views.forum, name='core-forum'),
		url = reverse('core-forum')
		self.assertEqual(resolve(url).func, forum)
		self.assertEqual(resolve(url).url_name, "core-forum")

		# response = self.client.get(reverse('core-forum'))
		# self.assertEqual(response.status_code, 200)
		# self.assertTemplateUsed(response, 'core/forum.html')

	# def test_comment(self):
	# 	# path('forum/', views.forum, name='core-forum'),
	# 	url = reverse('core-forumpage')
	# 	self.assertEqual(resolve(url).func, forumpage)
	# 	self.assertEqual(resolve(url).url_name, "core-forumpage/1")

	# 	response = self.client.get(reverse('core-forum'))
	# 	self.assertEqual(response.status_code, 200)
	# 	self.assertTemplateUsed(response, 'core/forum.html')\


	def test_expense(self):
		# path('expenses/', views.expenses, name='core-expenses'),
		url = reverse('core-expenses')
		self.assertEqual(resolve(url).func, expenses)
		self.assertEqual(resolve(url).url_name, "core-expenses")

		# response = self.client.get(reverse('core-expenses'))
		# self.assertEqual(response.status_code, 200)
		# self.assertTemplateUsed(response, 'core/expenses.html')


	# def test_expensedetail(self):
	# 	# path('expenses/', views.expenses, name='core-expenses'),
	# 	url = reverse('core-expensedetailpage')
	# 	self.assertEqual(resolve(url).func, expensedetailpage)
	# 	self.assertEqual(resolve(url).url_name, "core-expensedetailpage")

	# 	# response = self.client.get(reverse('core-expenses'))
	# 	# self.assertEqual(response.status_code, 200)
	# 	# self.assertTemplateUsed(response, 'core/expenses.html')



	def test_vets(self):
		# path('findvet/', views.findvet, name='core-findvet'),
		url = reverse('core-findvet')
		self.assertEqual(resolve(url).func, findvet)
		self.assertEqual(resolve(url).url_name, "core-findvet")

		# response = self.client.get(reverse('core-findvet'))
		# self.assertEqual(response.status_code, 200)
		# self.assertTemplateUsed(response, 'core/findvet.html')
