from django.urls import path
from . import views

urlpatterns = [
    path('apptest/', views.Myfun),
    path('apphome/', views.Home),
    path('appstore/', views.Store),
]
