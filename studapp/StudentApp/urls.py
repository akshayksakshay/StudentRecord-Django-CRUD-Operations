from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.homepage, name='home'),
    path('dashboard/',views.studdash, name = 'dashboard'),
    path('add/', views.addstud, name='add'),
    path('edit/<pk>/', views.editdata, name='edit'),
    path('delete/<pk>/', views.deletedata, name='delete'),
    path('register/',views.registration,name='register'),
    path('logoutuser/',views.logoutuser,name='logoutuser'),
    path('marklist/',views.marklist,name='marklist'),
    path('addmark/<sname>',views.addmarklist,name='addmark'),
    path('deletemark/<pk>',views.deletemarklist,name='deletemark'),
    path('filterdept/<slug:data>', views.filterdept, name='filterdept'), #<slug:data> is used to pass a string along with url
]