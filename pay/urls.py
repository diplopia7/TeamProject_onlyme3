import view as view
from django.urls import path
from . import views

urlpatterns = [
    path('pay/', views.pay, name='pay'),
    path('payok/', views.payok, name='payok'),
    path('buy/', views.buy, name='buy'),
    path('page/', views.page, name='page'),
]