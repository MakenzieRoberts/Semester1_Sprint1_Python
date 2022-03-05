# [ *** Delete after reading ***
# [ *** Here is the non-calculation function for Project 1 - Python Program ***


def dollar_format(num):
    # Written By: Makenzie Roberts
    # Last Edited: Feb 28, 2022

    # Description:
    #   This function formats a numerical value to display as a dollar value.

    # Parameters:
    #   The numerical value that will be formatted.

    # Returns:
    #   Returns the numerical value as a string, formatted to look like a dollar value.
    #   Eg. The argument 123456 is returned as $123,456.00

    formatStr = "${:,.2f}".format(num)

    return formatStr

