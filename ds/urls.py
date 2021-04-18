# -*- coding: utf-8 -*-
"""
URL config for the ds (main) app
"""

from django.urls import path

from ds import views

app_name = 'ds'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('process/', views.process, name='process'),
    path('settings/', views.settings, name='settings'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
