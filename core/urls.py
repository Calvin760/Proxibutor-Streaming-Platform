from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('release', views.release, name='release'),
    path('music_collection', views.music_collection, name='music'),
    path('about', views.about, name='about'),
    path('account', views.account, name='account'),
    path('update_account', views.update_account, name='account'),
    path('change_password', views.change_password, name='account'),
    path('artist_detail', views.artist_detail, name='streaming'),
    path('profile', views.profile, name='profile'),
    path('profile/<int:artist_id>/', views.profile, name='profile'),
    path('music2', views.music2, name='music2'),
    path('index2', views.index2, name='index2'),
    path('artist_profiles', views.artist_profiles, name='artistprofiles'),
    path('createArtist', views.create_artist_profile, name='createArtist'),
]