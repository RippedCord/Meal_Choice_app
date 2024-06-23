import functions


while True:
    loop_num = input("please type the number of the opperation you'd like to perform: \n 1. add a new meal \n 2. remove or edit a meal \n 3. create a new set of meals for the week")
    if loop_num =="1":
        functions.add_meal()
        
    elif loop_num =="2":
        functions.meal_remove()
    elif loop_num == "3":
        functions.meal_plan()
    else:
        continue