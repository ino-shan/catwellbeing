from django.contrib.auth.models import User
from django.test import TestCase
# python manage.py test users/tests
class UserTest(TestCase):
	def setUp(self):
		the_user = User.objects.create_user(username="inoshan", email="inoshan@yahoo.com", password="BA3bfuf3S", first_name="Inoshan", last_name="Inoshan")

	def tearDown(self):
		User.objects.all().delete()

	def test_user_variables(self):
		the_user = User.objects.get(username="inoshan")
		self.assertEqual(the_user.email,"inoshan@yahoo.com")
		self.assertEqual(the_user.first_name,"Inoshan")
		self.assertEqual(the_user.last_name,"Inoshan")

	def test_user_exist(self):
		the_user = User.objects.filter(username="inoshan").exists()
		self.assertTrue(the_user)

	def test_update_db(self):
		the_user = User.objects.get(username="inoshan")
		the_user.first_name = "Bruce"
		the_user.save()
		the_user = User.objects.get(username="inoshan")
		self.assertEqual(the_user.first_name,"Bruce")