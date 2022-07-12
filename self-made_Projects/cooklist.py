# Make a random list of what to cook today (healthy food ) or (Heavy food)

# 1- def for healthy and Heavy food
# 2- varibales for Breakfast, Lunch, dinner
# 3- user input for what to cook today


import random
from food import *


h = '\n\n have a good meel !'.title()

def healthy_food() :
    
    Breakfast = random.choice(['Eggs', 'Greek yogurt', 'Oats', 'Oatmeal', 'Chia seeds', 'Berries', 'Cottage cheese', 'Whole wheat toast' ])
    Lunch = random.choice(['Pasta salads', 'Soups and chili', 'Chicken salad', 'Burritos bowls', 'paninis', 'quiche']).capitalize()
    Dinner = random.choice(['beef casserole', 'beef steak', 'grilled', 'Vegetabel and soup/stew', 'Tacos', 'shawirma']).capitalize()

    return f'Your cook list for today \n for Breakfast : {Breakfast} \n for Lunch : {Lunch} \n for Dinner : {Dinner} ' 

def heavy_food() :
    
    Breakfast = random.choice(['Whole fat milk', 'cream', 'cheese', 'avocado', 'nuts', 'seeds', 'nut butters', 'eggs']).capitalize()
    Lunch = random.choice(['salmon meal prep with veggies','Pesto grilled cheese ', 'bacon, tomato & avocado Sandwich', 'Peanut Chicken', 'sheet pan chicken', 'Shawarma', 'thai noodle bowl', 'sheet pan cashew chicken']).capitalize()
    Dinner = random.choice(['Sheet Pan Peanut Chicken & Veggies', 'peanut chicken rice', 'chicken cheese broccoli', 'steak fajita salad', 'cinnamon roll pancakes', 'cauliflower mac & cheese']).capitalize()

    return f'Your cook list for today \n for Breakfast : {Breakfast} \n for Lunch : {Lunch} \n for Dinner : {Dinner} ' 


userchoice = input('Do you whant your day Healthy/Heavy? : ').lower()


if userchoice == 'healthy' :
    
    print(healthy_food(), h)

elif userchoice == 'heavy' : 

    print(heavy_food(), h)

else : 

    print('This type is not exist in our list')