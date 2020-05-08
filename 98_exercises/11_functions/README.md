# Functions Exercises

###### **Note**: Make sure that you have Text Editor installed


### Functions

#### Ex 1. 

Write a program that defines a function which receives two parameters : an array and a number
    - Print the Array’s Sum
    - returns :
      -  True – if the number is greater than array length
      -  False - if the number is lower or equal than array length

#### Ex2. 

Write a function called “Add” that receives two numbers and returns their Sum. Write a
function called “Mul” that receives two numbers and returns their Multiply only by calling “Add”
function,WITHOUT the “*” operator.

#### Ex3.

Write a function that receives a number ( 2 power of some number - 16,64,256...) and print it’s
half in recursion . E.g: 32 - > Print : 32,16,8,4,2,1

#### Ex4.

Write a function that recives a collection (list, tuple, set or dict) and deconstructs is. e.g.:
Use next list [ 2 , “ Hello” , [ “Bye” , [ 6, 3, 1, { “nums” : [10,20,30] } ] ] ], and deconstruct it with your function.

#### Ex5.

Write a program that converts kilometers to miles. The plan consists of two parts:
  
  - A function called convert_km_to_miles. The function accepts several miles and converts to miles according to the following formula: miles = miles * 0.6214. The function returns the value of calculated miles.
  - A primary program that asks the user to enter a number of miles, calls the convert_km_to_miles function, recovers the value in miles and prints the number of miles.

#### Ex6.

Write a plan that calculates the income tax on salary. The program consists of two parts:
  - A function named calc_tax. The function receives a salary and returns the income tax calculated according to the following steps:
      - Up to a payroll of 5220 the tax rate is 10%.
      - Between 5221 and 8920 the tax rate is 14%
      - Between 8921 and 13860 the tax rate is 21%
      - Over 13860 tax rate is 31%
  -  Main program. The program will ask the user to make a salary, call for a calc_tax position, get back the calculated tax and print it

#### Ex7.

Write a program that checks the faster running time among different runners. The program consists of two parts:
  - A function called find_fastest_time. The function receives a list of run times and returns the fastest run time.
  - Main program. The program asks the user to enter 10 run times. Run time is defined as a decimal fraction (two digits after the point). One can assume that the user enters correct values. The program puts the running times into the list, calls for find_fasters_time, gets back the fastest running time and prints it using the following message: The fastest time is: ___


#### Ex8.

Write a program that will absorb a number and call the function is_primt. The function checks whether the number is prime and inserts its divisions into the list. The master program prints the divisor of the narrator, if it is not initial.

#### Ex9.

Write a program that checks the percentage of failures (the percentage of grades below 60). The program consists of 3 parts:
  - The ask_for_grades posture. The function asks the user for the number of grades to be taken and accordingly receives scores from the user. If the user has entered a score less than zero or greater than 100, an appropriate message must be given and the grade requested again. The function puts the grades in the list. The function returns the list.
  - A function called calc_failures. The function gets the list from section a and counts how many failures there are. Focation returns the percentage of failures (the percentage must be calculated from the number of failures)
  - Main program. The program will do the following:
    - Call the function from section a to get the list of grades.
    - Call the function from section b to get the percentage of failures
    - Prints the percentage of failures


#### Ex10.

Write a program that prints the first 20 numbers. Please use written in the previous Exercise.

#### Ex11.