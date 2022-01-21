# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 11:53:08 2022
"""

from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.about, name='about')]
