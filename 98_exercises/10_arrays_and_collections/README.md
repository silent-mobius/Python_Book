# Collections and Arrays Exercises

###### **Note**: Make sure that you have Text Editor installed


#### Ex0.

Write a Python program that iterate over elements repeating each as many times as its count.

#### Ex1.

Write a Python program to find the most common elements and their counts of a specified text.

#### Ex2.

Prompt the user to enter numbers (one by one) and insert those numbers into array, until the the user enters a number that is bigger than 10
    •  Verify that there aren’t any elements that repeat themselves 
    •  Remove the numbers one by one and print them 

#### Ex3.

Implement a data structure that will hold a key:value pairs in a variable named:”students”, the key should be an integer and the value should be a list with AT LEAST three INTEGER elements, prompt the user to enter an ID, validate if the ID is in the dictionary and print out the highest grade in the value’s list.

#### Ex4.

Build the following array:
[ 2 , “ Hello” , [ “Bye” , [ 6, 3, 1, { “nums” : [10,20,30] } ] ] ] and Replace the [10,20,30] array with their sum (60)

#### Ex5.

Write a program that asks the user to enter the total sales of a store each weekday. Each day's sales must be entered in the list (total of 7 entries). The plan must calculate the total sales per week and show the result.

#### Ex6.

Write a program that asks the user to enter monthly precipitation for 12 months. All data must be included in the list. The plan must show total rainfall per year, average rainfall per month, maximum and minimum rainfall.

#### Ex7.

Write a program that asks the user for the weekly number of 10 employees and puts them on the list. Each worker earns 8000 shmekel per hour. Print your employees' salaries.

#### Ex8.

Write a program that produces the following list: x = [3,5, "aaa", 7,99, "bbb"]. All non-numbered items must be deleted from the existing list. After running the program, the list will look like x = [3,5,7,99].

#### Ex9.

Write a program that produces the following list: x = [3,5, "aaa", 7,99, "bbb"]. A new list must be created that contains only the non-numeric values. The new list will look like this: y = [“aaa”, “bbb”].

#### Ex10.

Write a program that asks the user to enter 10 different numbers. The numbers must be entered in a list. Before entering any number, check if the number has already been entered and if yes, please give notice that the number exists and not enter the number in the list.

#### Ex11.

Write a program that ran on the following list x = [2,5,6,4,5,5,3,2,7,8] and create a new list that includes all the original non-5 elements.

#### Ex12.

Write a program that receives from the user 5 integers. The data must be entered into a list. The program runs on the list and multiplies each number by 2. The new list must be printed.

#### Ex13.

Write a program that asks the user to enter 10 numbers. The numbers are put into a list. Then go over the list and exclude any number less than 5 into a new list

#### Ex14.

Write a program that creates any list of length 10. Print the following sub-lists:

    - The first three elements on the list
    - The last three elements on the list
    - All parts of the list except the first
    - All parts of the list except the last one

#### Ex15.

Write a program that captures sentences from the user and keeps them on the list. The program will stop absorbing when the user enters the word: STOP. All sentences must be printed in reversed fasion.

#### Ex16.

Write a program that captures 10 integers from the user and saves them in the list. The program will print "Even" if there are more even numbers in the list, "odd" if there are more odd numbers and "same" if there are the same number of odd and even numbers

#### Ex17.

Write a program that receives numbers from the user and saves them in the list. The program will pull out the local maximum points in the list (that is, a point whose values to the right and left are lower). Print all the maximum points in the form of index: value. For the list: x1 = [2,5,1,3,7,8,9,2,3,6]. The program will print the following points: 5,9.


#### Ex18.

Create a dictionary called days, which maps the day of the week to numbers 1-7. The dictionary will look like this:
{'Sunday': 1, 'Monday': 2, 'Thurthday': 3, 'Wendsday': 4, 'Thurthday': 5, 'Friday': 6, 'Saturday': 7}
    - Write a position that receives the dictionary as a parameter. The function prompts the user one day a week and returns the appropriate number or 0 if the user has typed an error.

#### Ex19.

Create a dictionary called runners_time that contains IDs and runtime in seconds. Write a function called build_runner_times. The function requests the data from the user and builds a dictionary. The function returns the dictionary to the main program. The main program prints the dictionary.

#### Ex20.

a. Create a dictionary named - d1, which has three pairs of key-values, so that there is one key of each data type: str, int, float.
b. Create a blank dictionary named d2
c. Go through the loop on all keys of d1, and enter them as values into d2. The keys of d2 will be the values from d1 (operation of inversion of keys and values)
d. The operation may fail. If it fails, try to understand when the action will fail and when it will succeed.

#### Ex21.

- Write a function called build_encrypt_code. The function builds an encryption dictionary that consists of hundreds as a key and a number as a value. For example:
{'a': 7, 'b': 1, 'c': 6, 'd': 0, 'e': 5, 'f': 4, 'g': 9, 'h': 3, ' I ': 2,' j ': 8}
- Write a caption called encrypt. The function obtains the dictionary from paragraph a and a string consisting of one word, and encrypts the string according to the dictionary. If the letter does not exist in the dictionary, it should be written without encryption. Upper and lower case letters are translated in the same way. For example, the letters a and a will be assigned to number 7.
- Write a master program that asks the user for a string and uses both functions to encrypt the string. The program will print the encrypted string.

#### Ex22.

In this exercise, we will write a code that will simulate an auto grocery manager.
Create a dictionary called groceries, with the keys and values:
“Banana”: 6, “orange”: 5, “apple”: 0
Set up a dictionary called stock, with the following keys and values:
“Banana”: 6, “apple”: 0, “orange”: 32, “pear”: 15
Set a dictionary called prices, with the following keys and values:
“Banana”: 4, “apple”: 2, “orange”: 1.5, “pear”: 3
Define a function named compute_bill. The function will receive two parameters - product name and desired quantity. If the items are in stock, the function will print a payment amount. Otherwise the function will print that there are no such products in stock.
Write a plan to buy from the grocery store all the groceries in the shopping list represented by the groceries dictionary.


#### Ex23.

Suppose these are tax steps:
- Over 10000 and less than 20000: 30%
- Over 20000 and less than 30000: 40%
- Above 30000: 50%
- Write a function that receives a person's salary and prints the tax on that person to pay.
- Write a program that captures 30 users' names and their salaries and saves a dictionary that maps employee names (keys) to their salaries (values). The plan will print how much tax each employee owes

#### Ex24.

Write a function called dict_reverse, which accepts a dictionary and returns a new dictionary that is "inverted" to the previous dictionary, meaning that the keys in the first dictionary are the values of the second dictionary and vice versa. In the dictionary, as is well known, the keys are necessarily different, but the values can be the same. In the case of two or more identical entries, we will insert the various keys into the list and the list will be the value of the new dictionary. example:
D1 = {'a': 1, 'b': 1, 'c': 1, 'd': 2}
D2 = reverse_dict (d1)
Print (d2)
{1: ['a', 'b', 'c'], 2: 'd'}

#### Ex25.



<!--
1. Write a program that receives two strings from the user: one for name and the other for password. If the login information (name and password) matches one of the users of the table below, type "Welcome Master", otherwise "INTRUDER ALERT" should be printed. The proper login details are:

```bash
Name: apple, password: red
Name: lettuce, Password: green
Name: lemon, Password: yellow
Name: orange, Password: orange
```

2. Write a Python program that receives a list of 20 scores through the command line. The program must calculate the average grades and print all grades above the average. For example:
```py
python3 script.py 99 90 15 28 38 44 50 81 79 60 99 90 15 28 38 44 50 81 79 60
```
**printout**:
```bash
99 90 81 79 60 99 90 81 79 60
```
> *_Hint_*: The sys.argv special list represents all the parameters passed to Python through the command line. Try to find it and figure out how to use it to solve the exercise.

3. Given a file named hosts containing rows of hostname = ipaddress form. For example, the contents of such a file might look like this:
```bash
work = 10.0.0.2
router = 10.0.0.1
mycar = 10.0.0.5
home = 194.90.2.1
```
Write a program that receives from the user a list of computers names as command line parameters and prints all the computers IP addresses in the list. If one of the names does not appear in the file, an appropriate error message should be displayed.

4. Write a program that identifies anagrams in a word list: two words are an anagram if they have the same letters in a different order. The program will take a path to a file containing a list of words and print all words that are one anagrams of each other in the same line.

For example, if the file contains the lines:
```bash
add
dad
help
more
Rome
```
**Printout**:
```bash
add dad
help
more rome
```
> (The order of lines in the output is not important, as is the order of words in each line).

-->