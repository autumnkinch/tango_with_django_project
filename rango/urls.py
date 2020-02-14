# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 20:33:11 2020

@author: NFLATE_MOA4
"""

from django.urls import path
from django.conf import settings
from rango import views
from django.conf.urls.static import static

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
]
