import csv
import os

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
    

def meal_plan():
    days = int(input("how many days do you need meals for?"))
    