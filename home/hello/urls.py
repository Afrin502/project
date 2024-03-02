from django.contrib import admin
from django.urls import path
from hello import views

urlpatterns = [
    path('',views.index,name="hello"),
    path('contect',views.contect,name='contect')
]
