# -*- coding: utf-8 -*-
"""BMI calculator.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gjlEjkR6un-Kxz5-kKXkhfclV11zuY8u

# BMI Calculator
# This program calculates the Body Mass Index (BMI) based on user input and provides a health assessment.
# It ensures valid input and categorizes BMI into underweight, normal weight, overweight, or obesity.
"""

# Function to get valid user input, ensuring it is a positive number
def get_valid_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: Value must be greater than zero. Please try again.")
            else:
                return value
        except ValueError:
            print("Error: Please enter a valid number.")

# Get user input
weight = get_valid_input("Enter your weight in kilograms: ")
height = get_valid_input("Enter your height in meters: ")

# Calculate BMI
BMI = weight / (height ** 2)

# Determine BMI category
if BMI < 18.5:
    category = "Underweight"
elif 18.5 <= BMI <= 24.9:
    category = "Normal weight"
elif 25 <= BMI <= 29.9:
    category = "Overweight"
else:
    category = "Obesity"

# Display results
print(f"\nYour BMI is: {BMI:.2f}")
print(f"Health Assessment: {category}")



