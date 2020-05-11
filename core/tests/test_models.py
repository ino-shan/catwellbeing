from django.test import TestCase
from django.contrib.auth.models import User
from core.models import Cat, Reminder, MedicalRecord, Forum, Comment, Veterinary, Review, Expense
import datetime
# python manage.py test core/tests

class CatTest(TestCase):
	def setUp(self):
		the_user = User.objects.create_user(username="inoshan", email="inoshan@yahoo.com", password="BA3bfuf3S", first_name="Inoshan", last_name="Inoshan")
		the_cat = Cat.objects.create(owner=the_user,cat_name="Luna",gender="Female",birthday="2019-08-14",imagename="imgname",imageurl="imgurl",
			cat_weight=1.5,cat_weight_unit="KG",cat_breed="Strip",Spayed_Neutered=True,microchip_number="H57FH3BF83BF83B",insurance_provider="Argos",
			insurance_policy_number="UIFIUB2B423NB",clinic_name="PETS4VETS")
		the_cat = Cat.objects.create(owner=the_user,cat_name="Bob",gender="Male",birthday="2019-01-14",imagename="imgname2",imageurl="imgurl2",
			cat_weight=2.5,cat_weight_unit="KG",cat_breed="Black",Spayed_Neutered=True,microchip_number="H57FN43IONBOB",insurance_provider="Argos",
			insurance_policy_number="UIFU4BFU3NB",clinic_name="PETS4VETS")

	def tearDown(self):
		User.objects.all().delete()
		Cat.objects.all().delete()

	def test_cat_variables_1(self):
		the_user = User.objects.get(username="inoshan")
		the_cat = Cat.objects.get(owner=the_user, cat_name="Luna")
		self.assertEqual(the_cat.gender,"Female")	
		self.assertEqual(the_cat.cat_breed,"Strip")
		self.assertTrue(the_cat.Spayed_Neutered)
		self.assertEqual(the_cat.microchip_number,"H57FH3BF83BF83B")
		self.assertEqual(the_cat.insurance_provider,"Argos")
		self.assertEqual(the_cat.insurance_policy_number,"UIFIUB2B423NB")

	def test_cat_variables_2(self):
		the_user = User.objects.get(username="inoshan")
		the_cat = Cat.objects.get(owner=the_user, cat_name="Bob")
		self.assertEqual(the_cat.gender,"Male")		
		self.assertEqual(the_cat.cat_breed,"Black")
		self.assertTrue(the_cat.Spayed_Neutered)
		self.assertEqual(the_cat.microchip_number,"H57FN43IONBOB")
		self.assertEqual(the_cat.insurance_provider,"Argos")
		self.assertEqual(the_cat.insurance_policy_number,"UIFU4BFU3NB")

	def test_cat_exist(self):
		the_user = User.objects.get(username="inoshan")
		the_cat = Cat.objects.filter(owner=the_user).count()
		self.assertEqual(the_cat,2)

	def test_update_db(self):
		the_user = User.objects.get(username="inoshan")
		the_cat = Cat.objects.get(owner=the_user, cat_name="Bob")
		the_cat.cat_weight = 1.8
		the_cat.clinic_name = "Goddard"
		the_cat.save()
		the_cat = Cat.objects.get(owner=the_user, cat_name="Bob")
		self.assertEqual(the_cat.cat_weight,1.8)
		self.assertEqual(the_cat.clinic_name,"Goddard")

class ReminderTest(TestCase):
	def setUp(self):
		the_user = User.objects.create_user(username="inoshan", email="inoshan@yahoo.com", password="BA3bfuf3S", first_name="Inoshan", last_name="Inoshan")
		the_cat_1 = Cat.objects.create(owner=the_user,cat_name="Luna",gender="Female",birthday="2019-08-14",imagename="imgname",imageurl="imgurl",
			cat_weight=1.5,cat_weight_unit="KG",cat_breed="Strip",Spayed_Neutered=True,microchip_number="H57FH3BF83BF83B",insurance_provider="Argos",
			insurance_policy_number="UIFIUB2B423NB",clinic_name="PETS4VETS")
		the_cat_2 = Cat.objects.create(owner=the_user,cat_name="Bob",gender="Male",birthday="2019-01-14",imagename="imgname2",imageurl="imgurl2",
			cat_weight=2.5,cat_weight_unit="KG",cat_breed="Black",Spayed_Neutered=True,microchip_number="H57FN43IONBOB",insurance_provider="Argos",
			insurance_policy_number="UIFU4BFU3NB",clinic_name="PETS4VETS")
		the_remainder = Reminder.objects.create(owner=the_user,reminder_type="Appointment",reminder_cat=the_cat_1,reminder_email=True,reminder_repeat="Repeat (Off)",reminder_date="2020-06-07")
		the_remainder = Reminder.objects.create(owner=the_user,reminder_type="Appointment",reminder_cat=the_cat_2,reminder_email=False,reminder_repeat="Repeat (On)",reminder_date="2020-06-07")

	def tearDown(self):
		User.objects.all().delete()
		Cat.objects.all().delete()
		Reminder.objects.all().delete()

	def test_reminder_variables_1(self):
		the_user = User.objects.get(username="inoshan")
		the_cat = Cat.objects.get(owner=the_user, cat_name="Luna")
		the_remainder = Reminder.objects.get(owner=the_user, reminder_cat=the_cat)
		self.assertEqual(the_remainder.reminder_type,"Appointment")
		self.assertEqual(the_remainder.reminder_email,True)
		self.assertEqual(the_remainder.reminder_repeat,"Repeat (Off)")

	def test_reminder_variables_2(self):
		the_user = User.objects.get(username="inoshan")
		the_cat = Cat.objects.get(owner=the_user, cat_name="Bob")
		the_remainder = Reminder.objects.get(owner=the_user, reminder_cat=the_cat)
		self.assertEqual(the_remainder.reminder_type,"Appointment")
		self.assertEqual(the_remainder.reminder_email,False)
		self.assertEqual(the_remainder.reminder_repeat,"Repeat (On)")

	def test_update_db_1(self):
		the_user = User.objects.get(username="inoshan")
		the_cat = Cat.objects.get(owner=the_user, cat_name="Luna")
		the_remainder = Reminder.objects.get(owner=the_user, reminder_cat=the_cat)
		the_remainder.reminder_type = "Vaccination"
		the_remainder.reminder_email = False
		the_remainder.reminder_repeat = "Repeat (On)"
		the_remainder.save()

		the_remainder = Reminder.objects.get(owner=the_user, reminder_cat=the_cat)
		self.assertEqual(the_remainder.reminder_type,"Vaccination")
		self.assertNotEqual(the_remainder.reminder_email,True)
		self.assertEqual(the_remainder.reminder_repeat,"Repeat (On)")

	def test_update_db_1(self):
		the_user = User.objects.get(username="inoshan")
		the_cat = Cat.objects.get(owner=the_user, cat_name="Bob")
		the_remainder = Reminder.objects.get(owner=the_user, reminder_cat=the_cat)
		the_remainder.reminder_type = "Surgery"
		the_remainder.reminder_email = True
		the_remainder.reminder_repeat = "Repeat (Off)"
		the_remainder.save()

		the_remainder = Reminder.objects.get(owner=the_user, reminder_cat=the_cat)
		self.assertEqual(the_remainder.reminder_type,"Surgery")
		self.assertNotEqual(the_remainder.reminder_email,False)
		self.assertEqual(the_remainder.reminder_repeat,"Repeat (Off)")

class MedicalRecordTest(TestCase):
	def setUp(self):
		the_user = User.objects.create_user(username="inoshan", email="inoshan@yahoo.com", password="BA3bfuf3S", first_name="Inoshan", last_name="Inoshan")
		the_cat_1 = Cat.objects.create(owner=the_user,cat_name="Luna",gender="Female",birthday="2019-08-14",imagename="imgname",imageurl="imgurl",
			cat_weight=1.5,cat_weight_unit="KG",cat_breed="Strip",Spayed_Neutered=True,microchip_number="H57FH3BF83BF83B",insurance_provider="Argos",
			insurance_policy_number="UIFIUB2B423NB",clinic_name="PETS4VETS")
		the_cat_2 = Cat.objects.create(owner=the_user,cat_name="Bob",gender="Male",birthday="2019-01-14",imagename="imgname2",imageurl="imgurl2",
			cat_weight=2.5,cat_weight_unit="KG",cat_breed="Black",Spayed_Neutered=True,microchip_number="H57FN43IONBOB",insurance_provider="Argos",
			insurance_policy_number="UIFU4BFU3NB",clinic_name="PETS4VETS")
		the_record = MedicalRecord.objects.create(cat=the_cat_1,title="Title 1",description="description 1",imagename="img 1",imageurl="img 2")
		the_record = MedicalRecord.objects.create(cat=the_cat_2,title="Title 2",description="description 2",imagename="img 3",imageurl="img 4")

	def tearDown(self):
		User.objects.all().delete()
		Cat.objects.all().delete()
		MedicalRecord.objects.all().delete()

	def test_record_variables_1(self):
		the_user = User.objects.get(username="inoshan")
		the_cat = Cat.objects.get(owner=the_user, cat_name="Luna")
		the_record = MedicalRecord.objects.get(cat=the_cat)
		self.assertEqual(the_record.title,"Title 1")
		self.assertEqual(the_record.description,"description 1")

	def test_record_variables_2(self):
		the_user = User.objects.get(username="inoshan")
		the_cat = Cat.objects.get(owner=the_user, cat_name="Bob")
		the_record = MedicalRecord.objects.get(cat=the_cat)
		self.assertEqual(the_record.title,"Title 2")
		self.assertEqual(the_record.description,"description 2")

	def test_update_db_1(self):
		the_user = User.objects.get(username="inoshan")
		the_cat = Cat.objects.get(owner=the_user, cat_name="Luna")
		the_record = MedicalRecord.objects.get(cat=the_cat)
		the_record.title = "New Title 1"
		the_record.description = "New description 1"
		the_record.save()

		the_record = MedicalRecord.objects.get(cat=the_cat)
		self.assertEqual(the_record.title,"New Title 1")
		self.assertEqual(the_record.description,"New description 1")

	def test_update_db_1(self):
		the_user = User.objects.get(username="inoshan")
		the_cat = Cat.objects.get(owner=the_user, cat_name="Bob")
		the_record = MedicalRecord.objects.get(cat=the_cat)
		the_record.title = "New Title 2"
		the_record.description = "New description 2"
		the_record.save()

		the_record = MedicalRecord.objects.get(cat=the_cat)
		self.assertEqual(the_record.title,"New Title 2")
		self.assertEqual(the_record.description,"New description 2")


class ForumTest(TestCase):
	def setUp(self):
		the_user = User.objects.create_user(username="inoshan", email="inoshan@yahoo.com", password="BA3bfuf3S", first_name="Inoshan", last_name="Inoshan")
		the_forum = Forum.objects.create(owner=the_user,title="Title 1",description="description 1",created_at="2019-05-14")
		the_forum = Forum.objects.create(owner=the_user,title="Title 2",description="description 2",created_at="2019-03-16")

	def tearDown(self):
		User.objects.all().delete()
		Forum.objects.all().delete()

	def test_forum_variables_1(self):
		the_user = User.objects.get(username="inoshan")
		the_forum = Forum.objects.get(owner=the_user,title="Title 1")
		self.assertEqual(the_forum.description,"description 1")
		# self.assertEqual(the_forum.created_at,"2019-05-14")

	def test_forum_variables_2(self):
		the_user = User.objects.get(username="inoshan")
		the_forum = Forum.objects.get(owner=the_user,title="Title 2")
		self.assertEqual(the_forum.description,"description 2")
		# self.assertEqual(the_forum.created_at,"2019-05-14")

	def test_forum_exist(self):
		the_user = User.objects.get(username="inoshan")
		the_forum = Forum.objects.filter(owner=the_user).count()
		self.assertEqual(the_forum,2)

	def test_update_db(self):
		the_user = User.objects.get(username="inoshan")
		the_forum = Forum.objects.get(owner=the_user, title="Title 1")
		the_forum.description = 'Title 3'		
		the_forum.save()
		the_forum = Forum.objects.get(owner=the_user, title="Title 1")
		self.assertEqual(the_forum.description,'Title 3')
		
	def test_update_db(self):
		the_user = User.objects.get(username="inoshan")
		the_forum = Forum.objects.get(owner=the_user, title="Title 2")
		the_forum.description = 'Title 4'		
		the_forum.save()
		the_forum = Forum.objects.get(owner=the_user, title="Title 2")
		self.assertEqual(the_forum.description,'Title 4')


class CommentTest(TestCase):
	def setUp(self):
		the_user = User.objects.create_user(username="inoshan", email="inoshan@yahoo.com", password="BA3bfuf3S", first_name="Inoshan", last_name="Inoshan")
		the_forum = Forum.objects.create(owner=the_user,title="Title 1",description="description 1",created_at="2019-05-14")
		the_forum2 = Forum.objects.create(owner=the_user,title="Title 2",description="description 2",created_at="2019-06-14")
		the_comment = Comment.objects.create(forum=the_forum,owner=the_user,description="reply 1",created_at="2019-07-22")
		the_comment = Comment.objects.create(forum=the_forum2,owner=the_user,description="reply 2",created_at="2019-03-01")	

	def tearDown(self):
		User.objects.all().delete()
		Forum.objects.all().delete()
		Comment.objects.all().delete()

	def test_comment_variables_1(self):
		the_user = User.objects.get(username="inoshan")
		the_forum = Forum.objects.get(owner=the_user,title="Title 1")
		the_comment = Comment.objects.get(owner=the_user,forum=the_forum)		
		self.assertEqual(the_comment.description,"reply 1")
		# self.assertEqual(the_forum.created_at,"2019-05-14")

	def test_comment_variables_1(self):
		the_user = User.objects.get(username="inoshan")
		the_forum = Forum.objects.get(owner=the_user,title="Title 2")
		the_comment = Comment.objects.get(owner=the_user,forum=the_forum)		
		self.assertEqual(the_comment.description,"reply 2")
		# self.assertEqual(the_forum.created_at,"2019-05-14")

	def test_update_db_1(self):
		the_user = User.objects.get(username="inoshan")
		the_forum = Forum.objects.get(owner=the_user, title="Title 1")
		the_comment = Comment.objects.get(owner=the_user,forum=the_forum)
		the_comment.description = "reply 3"
		the_comment.save()

		the_comment = Comment.objects.get(owner=the_user, forum=the_forum)
		self.assertEqual(the_comment.description,"reply 3")
		self.assertNotEqual(the_comment.description,"reply 1")
	

	def test_update_db_1(self):
		the_user = User.objects.get(username="inoshan")
		the_forum = Forum.objects.get(owner=the_user, title="Title 1")
		the_comment = Comment.objects.get(owner=the_user,forum=the_forum)
		the_comment.description = "reply 3"
		the_comment.save()

		the_comment = Comment.objects.get(owner=the_user, forum=the_forum)
		self.assertEqual(the_comment.description,"reply 3")
		self.assertNotEqual(the_comment.description,"reply 1")
	

class ReviewTest(TestCase):
	def setUp(self):
		the_user = User.objects.create_user(username="inoshan", email="inoshan@yahoo.com", password="BA3bfuf3S", first_name="Inoshan", last_name="Inoshan")
		the_vet = Veterinary.objects.create(name="Pets 4 Vets")
		the_vet2 = Veterinary.objects.create(name="VetsRUs")
		the_review = Review.objects.create(owner=the_user,vet_clinic=the_vet,review_rating=4,review_text="Nice Review")
		the_review = Review.objects.create(owner=the_user,vet_clinic=the_vet2,review_rating=1,review_text="Bad Review")

	def tearDown(self):
		User.objects.all().delete()
		Veterinary.objects.all().delete()
		Review.objects.all().delete()

	def test_review_variables_1(self):
		the_user = User.objects.get(username="inoshan")
		the_vet = Veterinary.objects.get(name="Pets 4 Vets")
		the_review = Review.objects.get(owner=the_user,vet_clinic=the_vet)		
		self.assertEqual(the_review.review_rating,4)
		self.assertEqual(the_review.review_text,"Nice Review")
		# self.assertEqual(the_forum.created_at,"2019-05-14")

	def test_review_variables_1(self):
		the_user = User.objects.get(username="inoshan")
		the_vet = Veterinary.objects.get(name="VetsRUs")
		the_review = Review.objects.get(owner=the_user,vet_clinic=the_vet)		
		self.assertEqual(the_review.review_rating,1)
		self.assertEqual(the_review.review_text,"Bad Review")
		# self.assertEqual(the_forum.created_at,"2019-05-14")

	def test_update_db_1(self):
		the_user = User.objects.get(username="inoshan")
		the_vet = Veterinary.objects.get(name="Pets 4 Vets")
		the_review = Review.objects.get(owner=the_user,vet_clinic=the_vet)		
		the_review.review_rating = 1
		the_review.review_text = "Maybe not Nice Review"
		the_review.save()

		the_review = Review.objects.get(owner=the_user,vet_clinic=the_vet)
		self.assertEqual(the_review.review_text,"Maybe not Nice Review")
		self.assertNotEqual(the_review.review_text,"Nice Review")
		self.assertEqual(the_review.review_rating,1)
	

	def test_update_db_1(self):
		the_user = User.objects.get(username="inoshan")
		the_vet = Veterinary.objects.get(name="VetsRUs")
		the_review = Review.objects.get(owner=the_user,vet_clinic=the_vet)		
		the_review.review_rating = 3
		the_review.review_text = "Maybe not Bad Review"
		the_review.save()

		the_review = Review.objects.get(owner=the_user,vet_clinic=the_vet)
		self.assertEqual(the_review.review_text,"Maybe not Bad Review")
		self.assertNotEqual(the_review.review_text,"Bad Review")
		self.assertEqual(the_review.review_rating,3)
	

class ExpenseTest(TestCase):
	def setUp(self):
		the_user = User.objects.create_user(username="inoshan", email="inoshan@yahoo.com", password="BA3bfuf3S", first_name="Inoshan", last_name="Inoshan")
		the_expense = Expense.objects.create(title="Flea&Worm",cost=23,expense_date="2019-01-14",expender=the_user,expense_repeat="Repeat (Off)")
		the_expense2 = Expense.objects.create(title="Vaccination",cost=50,expense_date="2019-03-10",expender=the_user,expense_repeat="Daily")

	def tearDown(self):
		User.objects.all().delete()
		Expense.objects.all().delete()


	def test_expense_variables_1(self):
		the_user = User.objects.get(username="inoshan")
		the_expense = Expense.objects.get(expender=the_user, title="Flea&Worm")
		self.assertEqual(the_expense.cost,23)
		self.assertEqual(the_expense.expense_repeat,"Repeat (Off)")

	def test_expense_variables_1(self):
		the_user = User.objects.get(username="inoshan")
		the_expense = Expense.objects.get(expender=the_user, title="Vaccination")
		self.assertEqual(the_expense.cost,50)
		self.assertEqual(the_expense.expense_repeat,"Daily")
	
	
	def test_update_db_1(self):
		the_user = User.objects.get(username="inoshan")
		the_expense = Expense.objects.get(expender=the_user, title="Flea&Worm")		
		the_expense.cost = 2
		the_expense.expense_repeat = "Weekly"
		the_expense.save()

		the_expense = Expense.objects.get(expender=the_user, title="Flea&Worm")
		self.assertEqual(the_expense.cost,2)
		self.assertNotEqual(the_expense.cost,50)
		self.assertEqual(the_expense.expense_repeat,"Weekly")


	def test_update_db_1(self):
		the_user = User.objects.get(username="inoshan")
		the_expense = Expense.objects.get(expender=the_user, title="Vaccination")		
		the_expense.cost = 60
		the_expense.expense_repeat = "Yearly"
		the_expense.save()

		the_expense = Expense.objects.get(expender=the_user, title="Vaccination")
		self.assertEqual(the_expense.cost,60)
		self.assertNotEqual(the_expense.cost,50)
		self.assertEqual(the_expense.expense_repeat,"Yearly")