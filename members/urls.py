from django.contrib import admin
from django.urls import path
from members import views
urlpatterns = [
   path('',views.home,name="home"),
    path('signup',views.signup,name="signup"),
    path('login',views.handlelogin,name="handlelogin"),
    path('logout',views.handlelogout,name="handlelogout"),
   path('search',views.search,name="search"),
   path('content',views.content,name="content")
]
