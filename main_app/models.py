from django.db import models
from django.contrib.auth.models import User

# Model for food transactions
class FoodTransaction(models.Model):
    restaurant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    ingredient_name = models.CharField(max_length=100)
    ingredient_quantity = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.ingredient_name} - {self.ingredient_quantity}"

# Model for restaurants
class RestaurantProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

# Model for food acceptors
class FoodAcceptorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.organization_name

# Model for donation records
class FoodDonation(models.Model):
    donor = models.ForeignKey(RestaurantProfile, on_delete=models.CASCADE, related_name='donations')
    acceptor = models.ForeignKey(FoodAcceptorProfile, on_delete=models.CASCADE, related_name='received_donations')
    ingredient_name = models.CharField(max_length=100)
    quantity_donated = models.FloatField()
    donation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Donation of {self.ingredient_name} to {self.acceptor}"

# Model for AI predictions
class Prediction(models.Model):
    restaurant = models.ForeignKey(RestaurantProfile, on_delete=models.CASCADE, related_name='predictions')
    prediction_date = models.DateField(auto_now_add=True)
    predicted_food_waste = models.FloatField()  # Example: Predicted food waste amount
    prediction_details = models.TextField()  # Additional details or insights from the AI model

    def __str__(self):
        return f"Prediction for {self.restaurant.name} on {self.prediction_date}"
