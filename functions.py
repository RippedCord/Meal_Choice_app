import csv
import os
import pandas
import random


class meal:

    def __init__(self):
        while True:
            self.name = input("what is the name of the food you would like to add? ")
            confirm = input(f"{self.name}... is that correct? Y/N?").upper()
            if confirm == "Y":
                break
            else: 
                continue
        while True:
            self.size = input("is the meal small, medium or large? enter S,M or L").upper()
            if self.size in ["S","M","L"]:
                break
            else:
                continue
        self.attributes = input("any other attributes you want to add to this meal for better meal choice later? leave blank if none?")


def add_meal():
    new_meal = meal()
    headers = ["Name", "Size", "attributes"]
    file_exists = os.path.isfile("meal_list.csv")
    with open ("meal_list.csv","a") as meallist:
        writer = csv.DictWriter(meallist, fieldnames=headers)
        if not file_exists:
            writer.writeheader()
        else:
            writer.writerow({"Name":new_meal.name, "Size": new_meal.size, "attributes":new_meal.attributes})
    

    
def meal_remove():
    data = pandas.read_csv("meal_list.csv")
    data = data.reset_index = True
    print(data.to_string)
    while True:
        meal_num = int(input("what is the index number of the meal you would like to remove?"))
        print(data.iloc[meal_num])
        con = input("Is this the correct meal? Y/N ").upper()
        if con == "Y":
            data.drop(index=[meal_num])
            break
        else:
            if input("Return to the main menu? Y/N").upper() == "Y":
                break
            else:
                continue



def meal_plan():
    # Asks how many of each size meal is needed
    meals = input("how many meals do you need? S,M,L ")
    meals = meals.split()
    meals_list = [int(x) for x in meals]
    data = pandas.read_csv("meal_list.csv")

    final_smeal= []
    final_mmeal= []
    final_lmeal= []

    # Gets all the meals in vars by size
    smeal = data[data["Size"] == "S"]
    mmeal = data[data["Size"] == "M"]
    lmeal = data[data["Size"] == "L"]

    # Gets the correct number of meals for each size
    for _ in range(meals_list[0]):
        final_smeal.append(random.choice(smeal.to_dict("records")))
    
    for _ in range(meals_list[1]):
        final_mmeal.append(random.choice(mmeal.to_dict("records")))
    
    for _ in range(meals_list[2]):
        final_lmeal.append(random.choice(lmeal.to_dict("records")))

    # Prints all the meals in the plan
    ### maybe add an index for changing a meal for the user?
    print("Small meals:")
    for meal in final_smeal:
        
        print(meal["Name"])
    
    print("Medium meals:")
    for meal in final_mmeal:
        print(meal["Name"])
    
    print("Large meals:")
    for meal in final_lmeal:
        print(meal["Name"])