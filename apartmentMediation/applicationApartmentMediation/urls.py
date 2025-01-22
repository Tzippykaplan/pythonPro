from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.get_home_page),
    # path("add_seller/", views.add_seller),
    # path("add_buyer/", views.add_buyer),
    # path("/", views.get_home_page),
]