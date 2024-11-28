from django import forms
from .models import FoodTransaction, RestaurantProfile, FoodAcceptorProfile, FoodDonation, Prediction
from django.contrib.auth.models import User

# Form for food transactions
class FoodTransactionForm(forms.ModelForm):
    class Meta:
        model = FoodTransaction
        fields = ['ingredient_name', 'ingredient_quantity']

# Form for restaurant profile creation
class RestaurantProfileForm(forms.ModelForm):
    class Meta:
        model = RestaurantProfile
        fields = ['name', 'address', 'phone_number']

# Form for food acceptor profile creation
class FoodAcceptorProfileForm(forms.ModelForm):
    class Meta:
        model = FoodAcceptorProfile
        fields = ['organization_name', 'contact_person', 'phone_number']

# Form for food donations
class FoodDonationForm(forms.ModelForm):
    class Meta:
        model = FoodDonation
        fields = ['acceptor', 'ingredient_name', 'quantity_donated']

# Form for handling AI predictions
class PredictionForm(forms.ModelForm):
    class Meta:
        model = Prediction
        fields = ['predicted_food_waste', 'prediction_details']
