from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test),
    path('hello/', views.index),
    path('category-list/', views.get_all_categories, name="category_list")
]