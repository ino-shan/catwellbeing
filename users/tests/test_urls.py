from django.test import TestCase, Client
from django.urls import reverse, resolve
from users.views import *
from django.contrib.auth import views as auth_views
from django.contrib import admin


class UrlTest(TestCase):
	def setUp(self):
		self.client = Client()


	def test_register(self):
		# path('', user_views.register, name='register'),
		url = reverse('register')
		self.assertEqual(resolve(url).func, register)
		self.assertEqual(resolve(url).url_name, "register")
		response = self.client.get(reverse('register'))
	


	def test_profile(self):
		# path('profile/', views.profile, name='profile'),
		url = reverse('profile')
		self.assertEqual(resolve(url).func, profile)
		self.assertEqual(resolve(url).url_name, "profile")

		# response = self.client.get(reverse('profile'))
		# self.assertEqual(response.status_code, 200)
		# self.assertTemplateUsed(response, 'userse/profile.html')


	def test_logout(self):
		# path('logout/', user_views.views.logout, name='profile'),
		url = reverse('logout')
		self.assertEqual(resolve(url).func, logout_view)
		self.assertEqual(resolve(url).url_name, "logout")

		# response = self.client.get(reverse('logout'))
		# self.assertEqual(response.status_code, 200)
		# self.assertTemplateUsed(response, 'userse/logout.html')



	# def test_login(self):
	# 	# path('logout/', user_views.views.logout, name='profile'),
	# 	url = reverse('login')
	# 	self.assertEqual(resolve(url).func,  auth_views.LoginView.as_view(template_name='users/login.html', redirect_authenticated_user=True))
	# 	self.assertEqual(resolve(url).url_name, "login")

	# 	# response = self.client.get(reverse('logout'))
	# 	# self.assertEqual(response.status_code, 200)
	# 	# self.assertTemplateUsed(response, 'userse/logout.html')



	# def test_password_reset(self):
	# 	# path('logout/', user_views.views.logout, name='profile'),
	# 	url = reverse('password_reset')
	# 	self.assertEqual(resolve(url).func, auth_PasswordResetView.as_view(template_name='users/password_reset.html'))
	# 	self.assertEqual(resolve(url).url_name, "password_reset")

	# 	# response = self.client.get(reverse('logout'))
	# 	# self.assertEqual(response.status_code, 200)
	# 	# self.assertTemplateUsed(response, 'userse/logout.html')

	



