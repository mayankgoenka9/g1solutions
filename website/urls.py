from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='website-home'),
    path('contactus/', views.contactus,name='website-about'),
]