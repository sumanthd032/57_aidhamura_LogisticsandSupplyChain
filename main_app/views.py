from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import FoodTransaction, RestaurantProfile, FoodAcceptorProfile, FoodDonation, Prediction
from .forms import FoodTransactionForm, RestaurantProfileForm, FoodAcceptorProfileForm, FoodDonationForm, PredictionForm
from django.http import JsonResponse
import random  # Mocking AI predictions for demonstration

# View for the home page
def home(request):
    return render(request, 'home.html')

# View for the about page
def about(request):
    return render(request, 'about.html')

# User login view
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after login
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

# User logout view
def user_logout(request):
    logout(request)
    return redirect('login')

# Dashboard view
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')

    restaurant_profile = RestaurantProfile.objects.filter(user=request.user).first()
    food_donations = FoodDonation.objects.filter(donor=request.user)
    predictions = Prediction.objects.filter(restaurant=restaurant_profile)

    context = {
        'restaurant_profile': restaurant_profile,
        'food_donations': food_donations,
        'predictions': predictions,
    }
    return render(request, 'dashboard.html', context)

# View for adding a new food transaction
def add_food_transaction(request):
    if request.method == 'POST':
        form = FoodTransactionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Food transaction added successfully!')
            return redirect('dashboard')
    else:
        form = FoodTransactionForm()
    return render(request, 'add_food_transaction.html', {'form': form})

# View for creating or updating restaurant profiles
def create_or_update_restaurant_profile(request):
    if request.method == 'POST':
        form = RestaurantProfileForm(request.POST, instance=request.user.restaurantprofile if hasattr(request.user, 'restaurantprofile') else None)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Restaurant profile updated successfully!')
            return redirect('dashboard')
    else:
        form = RestaurantProfileForm(instance=request.user.restaurantprofile if hasattr(request.user, 'restaurantprofile') else None)
    return render(request, 'create_or_update_restaurant_profile.html', {'form': form})

# View for creating or updating food acceptor profiles
def create_or_update_food_acceptor_profile(request):
    if request.method == 'POST':
        form = FoodAcceptorProfileForm(request.POST, instance=request.user.foodacceptorprofile if hasattr(request.user, 'foodacceptorprofile') else None)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Food acceptor profile updated successfully!')
            return redirect('dashboard')
    else:
        form = FoodAcceptorProfileForm(instance=request.user.foodacceptorprofile if hasattr(request.user, 'foodacceptorprofile') else None)
    return render(request, 'create_or_update_food_acceptor_profile.html', {'form': form})

# View for creating food donations
def create_food_donation(request):
    if request.method == 'POST':
        form = FoodDonationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Food donation created successfully!')
            return redirect('dashboard')
    else:
        form = FoodDonationForm()
    return render(request, 'create_food_donation.html', {'form': form})

# AI model prediction view (mock implementation)
def ai_prediction(request):
    if request.method == 'POST':
        # Mocked prediction logic (replace with real AI model logic)
        predicted_waste = random.uniform(10, 100)  # Simulated prediction value
        prediction_details = f"Predicted food waste for this month: {predicted_waste:.2f} kg"
        
        # Create a new prediction record
        prediction = Prediction.objects.create(
            restaurant=request.user.restaurantprofile,
            predicted_food_waste=predicted_waste,
            prediction_details=prediction_details
        )
        prediction.save()
        messages.success(request, 'AI prediction made successfully!')
        return redirect('dashboard')
    return render(request, 'ai_prediction.html')

# API endpoint to retrieve AI predictions as JSON
def get_prediction_data(request):
    if request.user.is_authenticated:
        predictions = Prediction.objects.filter(restaurant=request.user.restaurantprofile)
        data = list(predictions.values('predicted_food_waste', 'prediction_details'))
        return JsonResponse({'predictions': data}, safe=False)
    else:
        return JsonResponse({'error': 'Unauthorized'}, status=401)
