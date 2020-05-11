from django.contrib import admin
from .models import Cat, Reminder, MedicalRecord, Forum, Comment, Veterinary, Expense, Review
# Register your models here.

admin.site.register(Cat)
admin.site.register(Reminder)
admin.site.register(MedicalRecord)
admin.site.register(Forum)
admin.site.register(Comment)
admin.site.register(Veterinary)
admin.site.register(Expense)
admin.site.register(Review)