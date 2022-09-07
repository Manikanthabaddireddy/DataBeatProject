import imp
from django.urls import path
from register.views import login_user,register

urlpatterns = [

path('user_login/',login_user),
path('register/',register),

]