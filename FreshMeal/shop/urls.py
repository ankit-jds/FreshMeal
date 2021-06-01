from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("aboutus/", views.aboutus, name="Shop About Us"),
    path("contactus/", views.contactus, name="Shop Contact Us"),
    path("order/", views.order, name="Shop order"),
    path("Store/", views.Store, name="Store"),
    path("project_info/", views.project_info, name="Project Info")
    ]
