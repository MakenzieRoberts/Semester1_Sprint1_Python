# [ *** Delete after reading ***
# | *** Makenzie's suggestions for this while True loop in the main menu program. ***
# [ *** Each suggestion is marked by a comment which explains my logic. ***

while True:
    #Display_Menu() # I suggest display menu goes here so it displays the menu options again after a function runs

    Choice = input("Enter choice: (1-5): ") # Nitpicking but we might wanna change this to "Enter choice(1-5): " :)
    if Choice == "1":
        Emp_Trav_Claim()
        continue # We should tell the program to jump to the top of the loop after the task is completed
    elif Choice == "2":
        Fun_Question()
        continue # We should tell the program to jump to the top of the loop after the task is completed
    elif Choice == "3":
        Strings_Dates()
        continue # We should tell the program to jump to the top of the loop after the task is completed
    elif Choice == "4":
        Graph_Monthly_Totals()
        continue # We should tell the program to jump to the top of the loop after the task is completed
    elif Choice == "5":
        print()
        print("Thank you for utilizing the \"Claims Processing System\", have a wonderful day.")
        break
    else:
        print("Not a valid choice - please re-enter")
        print() # I think an extra blank line here looks pretty