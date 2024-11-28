from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('about/', views.about, name='about'),  # About page
    path('login/', views.user_login, name='login'),  # Login page
    path('logout/', views.user_logout, name='logout'),  # Logout page
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard page
    path('add_food_transaction/', views.add_food_transaction, name='add_food_transaction'),  # Add food transaction page
    path('create_restaurant_profile/', views.create_or_update_restaurant_profile, name='create_restaurant_profile'),  # Create or update restaurant profile page
    path('create_food_acceptor_profile/', views.create_or_update_food_acceptor_profile, name='create_food_acceptor_profile'),  # Create or update food acceptor profile page
    path('create_food_donation/', views.create_food_donation, name='create_food_donation'),  # Create food donation page
    path('ai_prediction/', views.ai_prediction, name='ai_prediction'),  # AI prediction page
    path('get_prediction_data/', views.get_prediction_data, name='get_prediction_data'),  # API endpoint for AI predictions
]
