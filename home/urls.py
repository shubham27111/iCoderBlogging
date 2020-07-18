from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('search', views.search, name='search'),
    path('signUp', views.handelSignUp, name='handelSignUp'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout')
]
