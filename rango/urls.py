# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 20:33:11 2020

@author: NFLATE_MOA4
"""

from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
]
