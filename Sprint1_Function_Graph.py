

def Graph_Monthly_Totals():

    # Written By: Makenzie Roberts
    # Last Edited: Feb 28, 2022

    # Description:
    #   This function produces a graph for Monthly Claim Totals (Total($) vs Month).

    # Parameters:
    #   Does not require a parameter and does not accept any arguments.
    #   To gather the data needed to plot the graph, it asks for (and requires) user input.

    # Returns:
    #   Returns a graph, created using matplotlib library.

    # Create lists that contain data for X and Y axis
    month_list = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"]

    # Y is initialized and empty so we can append user input
    y = []

    # Welcome message
    print()
    print("------------------------------------")
    print("Option 4: Graph Monthly Claim Totals")
    print("------------------------------------")
    print()
    print("This option produces a line graph using the data you provide. (Total($) vs Month)")
    print("Please enter the claim total($) for each month of the year.")

    print()
    # Ask user to input for monthly totals, then append to y axis list
    monthNum = 0
    for month in range(1, 13):
        inputOk = False
        while not inputOk:
            try:
                monthValue = float(input("Enter the amount for {}: ".format(month_list[monthNum])))
                inputOk = True
            except:
                print(
                    "The value for {} must be a valid number and cannot contain special characters. Please re-enter.".format(
                        month_list[monthNum]))
            else:
                y.append(monthValue)
                monthNum += 1

    # Abbreviates month names to first 3 characters for easy display
    monthNum = 0
    month_abbrev_list = []
    for month in range(1, 13):
        abbrev = month_list[monthNum]
        abbrev = abbrev[0:3]
        month_abbrev_list.append(abbrev)
        monthNum += 1

    # Set up the graph
    xAxis = month_abbrev_list
    yAxis = y

    plt.plot(xAxis, yAxis, color='#10a674', linestyle='-', marker='o')
    plt.xlabel('Month')
    plt.ylabel('Total($)')
    plt.title('Monthly Claim Totals')
    plt.grid(True)

    # Prompts user to press any key to continue
    print()
    print("Close graph to return to main menu")
    input("Press any key to continue...")
    print()

    # Return/display the graph to the user 
    # (The return statement is blank because passing plt.show() through it made the
    # graph lag and stop responding when closed on other team members computers)
    
    plt.show()
    
    # Blank return statement is used to go back to main menu
    return

    
