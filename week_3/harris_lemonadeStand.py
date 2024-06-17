"""
Author: Leah Harris
Date: 06-14-24
File Name: harris_lemonadeStand.py
Description: Simple Python program that simulates a lemonade stand
"""

#function to calculate the cost of making lemonade
def calculate_cost(lemons_cost, sugar_cost):
    return lemons_cost + sugar_cost
#function to calculate the remaining profit
def calculate_profit(lemons_cost, sugar_cost, selling_price):
    ingredients_cost = lemons_cost + sugar_cost

    profit_per_cup = selling_price - ingredients_cost

    return profit_per_cup

""" Variables for testing """

lemons_cost = .20
sugar_cost = .35
selling_price = 1.00

total_cost = calculate_cost(lemons_cost, sugar_cost)
total_profit = calculate_profit(lemons_cost, sugar_cost, selling_price)

#Formatting the output 
output = "The total cost of making a cup of lemonde is ${0:.2f}\nThe remaining profit will be ${1:.2f}".format(total_cost, total_profit)
#Print output 
print(output)