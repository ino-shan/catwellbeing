from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	
    path('', views.home, name='core-home'),
    path('cats/', views.cats, name='core-cats'),
    path('findvet/', views.findvet, name='core-findvet'),
    path('reminders/', views.reminders, name='core-reminders'),
    path('expenses/', views.expenses, name='core-expenses'),
    path('forum/', views.forum, name='core-forum'),
    path('forumpage/<int:id>/', views.forumpage, name='core-forumpage'),
    path('expensedetailpage/<slug:expense>/', views.expensedetailpage, name='core-expensedetailpage'),
   
] 


if settings.DEBUG:
	urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
