"""
A few decision-making puzzles to solve using if/elif/else logic.
Do not call any of these functions from within this file... only do that by running the main.py file.
Your job is to complete the definitions of each function so that it achieves its indicated behavior.
"""

import math
import datetime


def get_year():
    """
    This function is given to you... it is used by the is_leap_year() function below.
    Do not modify this function.
      :returns: The current year, e.g. 2020
    """
    now = datetime.datetime.now()  # get the current time now
    year = now.year  # the current year
    return year


def is_square():
    """
    Asks the user to enter the width and height of an area in inches and determines whether it is square.
    Users can enter either integers or floating point numbers.

      :returns: True if square (i.e. if equal length and height), False otherwise.
    """
    #### write your solution for this function below here. ####
    width = float(input("What is the width?"))
    length = float(input("What is the length?"))
    if width == length:
        return True
    else:
        return False


def get_greatest():
    """
    Asks the user for two integers, and returns the number that is greatest, as an int.
    You are not allowed to use Python's builtin max() function for this.
    If both numbers are the same, return that number.

    :returns: the greatest of the two input numbers, as an int.
    """
    #### write your solution for this function below here. ####
    num_1 = int(input("Write the first number"))
    num_2 = int(input("Write the second number"))
    if num_1 >= num_2:
        return num_1
    else:
        return num_2

def get_bmi_category():
    """
    Asks the user to enter their height (in inches) and weight (in pounds), in that order, and then returns the user's BMI statistical category.
    Users can enter either integers or floating point numbers.

    The BMI formula was developed in the 1830s, and is still widely used today in public health policy, medical practice, and legislation.
    The formula for calculating BMI is 703 * weight / height^2.
    The BMI statistical categories are:
    - Very severely underweight (BMI < 15)
    - Severely underweight (15 <= BMI < 16)
    - Underweight (16 <= BMI <18.5)
    - Normal (18.5 <= BMI < 25)
    - Overweight (25 <= BMI < 30)
    - Moderately obese (30 <= BMI < 35)
    - Severely obese (35 <= BMI < 40)
    - Very severely obese (BMI >= 40)

      :returns: The name of the BMI statistical category, based on the inputted height and weight.
    """
    #### write your solution for this function below here. ####
    height = float(input("What is your height?(in inches)"))
    weight = float(input("What is your weight?(in pounds)"))
    BMI = (703 * weight) / (height**2)
    if BMI < 15:
        return "Very severely underweight"
    elif 15 <= BMI < 16:
        return "Severely underweight"
    elif 16 <= BMI <18.5:
        return "Underweight"
    elif 18.5 <= BMI < 25:
        return "Normal"
    elif 25 <= BMI < 30:
        return "Overweight"
    elif 30 <= BMI < 35:
        return "Moderately obese"
    elif 35 <= BMI < 40:
        return "Severely obese"
    elif BMI >= 40:
        return "Very severely obese"




def get_discount():
    """
    Imagine this scenario: a surgical mask distributor will give you a 20% discount on orders of 5000 or more.
    Each mask individually costs $5.
    This function asks the user how many masks they would like, and returns the total cost after applying any relevant discount
    The total cost must be rounded to the nearest integer and formatted as in "$4,000".

      :returns: The cost of the masks, after any discounts, e.g. "$4,000" for 1000 masks.
    """
    #### write your solution for this function below here. ####
    masks = int(input("How many maskss would you like?"))
    total_cost = masks ** 5
    if masks >= 5000:
        total_cost *= 0.8
    total_cost = round(total_cost)
    formatted_cost = "${:,.0f}.int(total_cost)"
    return formatted_cost


def is_leap_year():
    """
    Determines whether the current year is a leap year.
    Any year evenly divisible by 4 is a leap year, except century years such as 1900, 2000, 2100, etc. Only century years evenly divisible by 400 are leap years.

    :returns: True if the current year is a leap year, False otherwise.
    """
    year = (get_year())  # this line is given to you - the variable, year, holds the current year
    #### write your solution for this function below here. ####
    if (year % 4 == 0) or (year % 400 == 0):
        return True
    else:
        return False
