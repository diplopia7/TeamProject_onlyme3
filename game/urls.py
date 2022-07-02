from django.urls import path
from . import views


urlpatterns = [
    path('game_info/', views.game_info, name='game_info'),
    path('how_to_fight/', views.how_to_fight, name='how_to_fight'),
    path('main_menu/', views.main_menu, name='main_menu'),
    path('character/', views.character, name='character'),
    path('story1/', views.story1, name='story1'),
    path('story2/', views.story2, name='story2'),
    path('story3/', views.story3, name='story3'),
    path('내정/', views.내정, name='내정'),
    path('전투/', views.전투, name='전투'),
]