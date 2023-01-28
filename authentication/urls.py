from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('homez', views.home, name="home"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name="signout"),
    path('place',views.place,name="place"),
    path('reports',views.reports,name="reports"),
    path('reportsresult',views.reportsresult,name="reportsresult")
]