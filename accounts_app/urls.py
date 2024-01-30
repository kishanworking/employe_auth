

from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views



urlpatterns = [
    
    path('', views.SignupPage.as_view() ,name='signup'),
    path('login/',views.LoginPage.as_view() ,name='login'),
    path('home/',login_required(views.HomePage.as_view()) ,name='home'),
    path('logout/', login_required(views.LogoutPage.as_view()) , name='logout'),
    
]