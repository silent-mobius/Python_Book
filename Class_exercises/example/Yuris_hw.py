'''
Don't Judge Me Please.
Owner: Yuri Boiko.
Date: 11/11/2019
Version 2.3.0
Purpose: Home Work About calculating how old is the user into days.
'''
import time
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################


#INTRO

print("Owner: Yuri Boiko.\n"
      "Last edit: 11/11/2019\n"
      "Version: 2.3.0\n"
      "Purpose: Home work (Date_Calc)\n")
print("In this Program You'll enter today's date, and the date of your birth-date.\n"
      "The program will calculate the dates, and will print out how old are You in days.\n")
print("###RULES###\n"
      "Enter the dates in FULL format (day/month/year)\n"
      "EXAMPLE: 27/02/1978\n\n\n")
time.sleep(10)
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################



#Function

def year_calc (year_a,year_b): # this function convert years into days.
    return (year_a - year_b) * 365.2425

def month_calc (month_a,month_b): # this function convert months into days.
   return (month_a - month_b) * 30.44

def day_calc (day_a,day_b):
    return (day_a - day_b)

def input_check (var): # This function checks if the format of the user's_input is right.
    if "\\" in var:
        return var.split("\\")
    if "/" in var :
        return var.split("/")
    if "." in var :
        return var.split(".")
    if "," in var :
        return var.split(",")
    if "|" in var :
        return var.split("|")
    if " " in var :
        return var.split(" ")
    if "-" in var :
        return var.split("-")
    if "_" in var :
        return var.split("_")
    else:
        return "invalid input"

def welcome(date_now,date_birth): # this function ask the user to input dates.
    date_now = input("Please enter todays date: ")
    print("")
    date_birth = input("Please enter Your birth-date: ")
    print("")
    return date_now,date_birth

def split_calc(date_now_checked,date_birth_checked): # this function splits and using another functions to calculate the dates.
    year_days = year_calc(int(date_now_checked[2]), int(date_birth_checked[2]))
    month_days = month_calc(int(date_now_checked[1]), int(date_birth_checked[1]))
    day_days = day_calc(int(date_now_checked[0]), int(date_birth_checked[0]))
    return year_days,month_days,day_days

def ERROR (): # This Function used when the user's input ins't right.
    print("[invalid input] Please Start Again...")
    input("#\n#\n#\n#\npress \"ENTER\" to close the program.")

################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################

#__MAIN__

def __main__(): # this is the main table

    # Here the program creates some variable to be used.
    date_now, date_birth = False,False
    year_days, month_days, day_days = False,False,False
    date_now, date_birth = welcome(date_now, date_birth)

    # Here it uses the function "input_check()".
    date_now_checked = input_check(date_now)
    date_birth_checked = input_check(date_birth)

    # Here the program prints out if the user's input wasn't right.
    if len(date_now_checked) != 3:
        ERROR()
    elif len(date_birth_checked) != 3:
        ERROR()
    elif date_now_checked == "invalid input":
        ERROR()
    elif date_birth_checked == "invalid input":
        ERROR()

    # Here the program uses the function "split_calc()".
    elif date_now_checked and date_birth_checked != "invalid input":
        year_days, month_days, day_days = split_calc(date_now_checked, date_birth_checked)

        # Here the program uses all the variables it got from the "split_calc()" function, and adds them together into new variable.
        days_old = year_days + month_days + day_days

        #here the program checks if the result is positive or negative (if the result is negative, it converts the variable to a positive), and prints it out to the user.1616
        if days_old <= 0:
            days_old = days_old * -1
            print("You are", days_old, "days old.")
        else:
            print("You are", days_old, "days old.")
        input("#\n#\n#\n#\npress \"ENTER\" to close the program.")
    else:
        print("#ERROR#")
        input("#\n#\n#\n#\npress \"ENTER\" to close the program.")

################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################

#Starting the program.

__main__()