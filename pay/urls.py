from django.urls import path
from . import views

app_name='pay'
urlpatterns = [
    path('pay/', views.pay, name='pay'),
    path('buy/', views.buy, name='buy'),
    path('payok/', views.payok, name='payok'),
]