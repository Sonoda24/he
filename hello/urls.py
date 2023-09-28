# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 10:14:53 2023

@author: user
"""
from django.urls import path
 
from . import views
 
urlpatterns = [
    path('', views.index, name='index'),
]