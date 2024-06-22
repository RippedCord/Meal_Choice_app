import functions


while True:
    loop_num = input("please type the number of the opperation you'd like to perform: \n 1. add a new meal \n 2. remove or edit a meal \n 3. create a new set of meals for the week")
    if loop_num =="1":
        functions.add_meal()
        # function for adding a new meal
    #elif loop_num == "2":
        # function for removing or editing a meal
    #elif loop_num == "3":
        #function for making a meal plan
    else:
        continue