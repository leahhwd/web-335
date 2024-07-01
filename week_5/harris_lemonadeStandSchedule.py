"""
Author: Leah Harris 
Date: 06-29-2024
File Name: harris_lemonadeStandSchedule.py
Description: This program prints out tasks and days of the week
"""
tasks = ["Go shopping", "Make Lemonade", "Set up stand", "Sell lemonade", "Clean up"]

for task in tasks:
    print(task)

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for day in days:
    if day == "Sunday" or day == "Saturday":
        print(f"{day}: Off Day")
    else:
        print(f"{day}: {tasks[days.index(day)]}")

""" I had trouble getting this program to work correctly.
There is something wrong with my loop, but I cant figure out what, though I'm
sure it's a very simple solution. I tried using len, enumerate, creating another 
for loop. Nothing was exactly what I needed. Advice is appreciated
"""