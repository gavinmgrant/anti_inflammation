from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path("login", views.login_view, name="login"),
  path("logout", views.logout_view, name="logout"),
  path("register", views.register, name="register"),
  path("list", views.list, name="list"),
  path("food/<int:id>", views.add, name="add"),
]