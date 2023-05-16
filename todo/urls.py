
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('login',views.loginfunction,name="login"),
    path('',views.signup,name="signup"),
    path('signedup',views.signedup,name="signedup"),
    path('logout',views.logoutfunction,name="logout"),
    path('loggedup',views.loggedup,name="loggedup"),
    path('home',views.home,name="home"),
    path('add1',views.add1,name="add1"),
    path('checkbox',views.checkbox,name='checkbox'),
    path('delete',views.deleted,name="deleted")
]
