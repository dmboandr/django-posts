from django.contrib import admin
from django.urls import include, path
from . import views

"""
Это urls приложения posts
"""

urlpatterns = [
    path('django/', views.abcdef),
    path('home/', views.home, name="home"),  #
    # PATH CONVENTION
    path("<int:id>", views.post)
]