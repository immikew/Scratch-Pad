

if __name__ == "__main__":

    # Prompt user for their hours; need to convert from str to int in
    # order to work with teh user input as a numerical value
    number_of_hours = input("Please Enter the Number of Hours that you Worked: ")
    number_of_hours = int(number_of_hours)

    # Assuming there are 24 hours in a day
    # TODO: handle situation where number of hours is negative
    percentage_of_day = number_of_hours / 24 * 100

    print(f"The number of hours you worked is {percentage_of_day}%")


    # WAGE CALCULATOR
    
    # prompt user for their hourly wage

    # prompt user for number of hours they worked

    # calculate wage based on rate * hours