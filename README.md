Problem statement: Design an AI-powered system that allows restaurants to track and manage surplus food, predict future food demand to minimize waste, and connect with NGOs or food banks for efficient redistribution, promoting sustainability and addressing food insecurity through actionable insights and optimized logistics.

# Zero Plate - AI-Powered Food Management System

## Overview
Zero Plate is an AI-powered website designed to help restaurants manage food waste efficiently. It integrates data analytics, real-time insights, and an AI-driven recommendation system to optimize food usage, provide actionable suggestions for minimizing waste, and facilitate food donations to food acceptors. The project is built using Django for the backend, with a focus on user authentication, data visualization, AI model integration, and dynamic dashboards.

## Features
- **User Authentication**: Built-in Django user authentication for restaurant and food acceptor logins.
- **AI Integration**: Machine learning models to analyze historical data and provide recommendations for reducing food waste.
- **Dashboard**: An interactive, dynamic dashboard for restaurants to view real-time analytics and insights.
- **Food Donations**: A system for restaurants to donate surplus food to food acceptors.
- **Data Visualization**: Integration of charts and graphs to display restaurant data and trends.

## Installation
### Prerequisites
- Python 3.8 or higher
- Django 5.1.3 or higher
- Git

### Steps to Set Up
1. **Clone the repository**:
   ```bash
   git clone https://github.com/sumanthd032/57_aidhamura_LogisticsandSupplyChain.git

2. **Navigate to the Project Directory**
   ```bash
   cd 57_aidhamura_LogisticsandSupplyChain

3. **Set Up a Virtual Environment**
   ```bash
   python3 -m venv venv

4. **Activate the Virtual Environment**
   ```bash
   source venv/bin/activate

  
5. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

6. **Create a Superuser**
   ```bash
   python manage.py migrate
   
7. **Apply Database Migrations**
   ```bash
   python manage.py createsuperuser
   
7. **Run the Development Server**
   ```bash
   python manage.py runserver


