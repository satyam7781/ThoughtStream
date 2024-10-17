from django.urls import path
from . import views

 # Make sure to import your views

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),  # Home page showing tweet list
    path('create/', views.tweet_create, name='tweet_create'),  # Page to create a tweet

    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),  # Edit a specific tweet
    path('<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),  # Delete a specific tweet
    path('register/', views.register, name='register'),  # Registration page
    path('tweet/<int:tweet_id>/like/', views.like_tweet, name='tweet_like'),  # Like a tweet
    path('profile/', views.profile_view, name='profile'),  # Add this line
]
