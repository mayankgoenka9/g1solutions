from django.urls import path,include
from . import views

urlpatterns = [
    path('login/', views.login,name='login'),
    path('signup/', views.signup,name='signup'),
    path('logout/', views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('enquiry/',views.enquiry,name='enquiry'),
    path('send_enquiry/',views.send_enquiry,name='send enquiry'),
    path('close_enquiry/',views.close_enquiry,name='close enquiry'),
]