from django.urls import path, include
from . import views

app_name = 'chirp'

urlpatterns = [
    path('', views.index, name='index'),
    path('feed/', views.all_chirps, name='all_chirps'),
    path('chirp/', views.new_chirp, name='new_chirp'),
    path('like/<int:pk>', views.like, name='like'),
    path('user/<str:username>', views.user_chirp, name='user_chirp')
]