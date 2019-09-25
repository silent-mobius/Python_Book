# Python Loops

Loops are used to repeatedly execute a block of program statements. In Python, and in most of programming languages, there are two main types of loops: for loop and while loops.

## For loop

In Python for loop is used to iterate over the items of any sequence including the Python list, string, tuple etc. The for loop is also used to access elements from a container (for example list, string, tuple) using built-in function range(). 

 The for loop is also used to access elements from a container (for example list, string, tuple) using built-in function range().

Syntax:
```
for variable_name in sequence :
    statement_1
    statement_2
    ....
```
**Parameter:**

Name | Description
----- | ------
variable_name | It indicates target variable which will set a new value for each iteration of the loop.
sequence | A sequence of values that will be assigned to the target variable variable_name. Values are provided using a list or a string or from the built-in function range().
statement_1, | 
statement_2 ... | Block of program statements.

**Example: Python for loop** 
```python
 #The list has four elements, indices start at 0 and end at 3
 color_list = ["Red", "Blue", "Green", "Black"]
 for c in color_list:
        print(c)

Red
Blue
Green
Black
```

In the above example color_list is a sequence contains a list of various color names. When the for loop executed the first item (i.e. Red) is assigned to the variable c. After this, the print statement will execute and the process will continue until we reach the end of the list.

### Python for loop and range() function

The range() function returns a list of consecutive integers. The function has one, two or three parameters where last two parameters are optional. It is widely used in for loops. Here is the syntax.

range(a) : Generates a sequence of numbers from 0 to a, excluding a, incrementing by 1.

```python
range(a)
range(a,b)
range(a,b,c)
```

Syntax:

for <variable> in range(<number>): 

Example:
```python
 for a in range(4):
  print(a)
 
  0
  1
  2
  3
```

range(a,b): Generates a sequence of numbers from a to b excluding b, incrementing by 1.

Syntax:

for "variable" in range("start_number", "end_number"):

Example:
```python
 for a in range(2,7):
 print(a)

  2
  3
  4
  5
  6
```

range(a,b,c): Generates a sequence of numbers from a to b excluding b, incrementing by c.

Example:
```python
 for a in range(2,19,5):
  print(a)
 
 2
 7
 12 
 17
```

### Python for loop: Iterating over tuple, list, dictionary

Example: Iterating over tuple

The following example counts the number of even and odd numbers from a series of numbers.
```python
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
count_odd = 0
count_even = 0
for x in numbers:
        if x % 2:
    	     count_odd+=1
        else:
    	     count_even+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)
```

>Output:

Number of even numbers:4
Number of odd numbers: 5

In the above example a tuple named numbers is declared which holds the integers 1 to 9.

The best way to check if a given number is even or odd is to use the modulus operator (%).
The operator returns the remainder when dividing two numbers.
Modulus of 8 % 2 returns 0 as 8 is divided by 2, therefore 8 is even and modulus of 5 % 2 returns 1 therefore 5 is odd.

The for loop iterates through the tuple and we test modulus of x % 2 is true or not, for every item in the tuple and the process will continue until we rich the end of the tuple.
When it is true count_even increase by one otherwise count_odd is increased by one.
Finally, we print the number of even and odd numbers through print statements.

Example: Iterating over list

In the following example for loop iterates through the list "datalist" and prints each item and its corresponding Python type.
```python
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12],
{"class":'V', "section":'A'}]
for item in datalist:
   print ("Type of ",item, " is ", type(item))
```

>Output:

Type of  1452  is  <class 'int'>
Type of  11.23  is  <class 'float'>
Type of  (1+2j)  is  <class 'complex'>
Type of  True  is  <class 'bool'>
Type of  w3resource  is  <class 'str'>
Type of  (0, -1)  is  <class 'tuple'>
Type of  [5, 12]  is  <class 'list'>
Type of  {'section': 'A', 'class': 'V'}  is  <class 'dict'>

Example: Iterating over dictionary

In the following example for loop iterates through the dictionary "color" through its keys and prints each key.
```python
 color = {"c1": "Red", "c2": "Green", "c3": "Orange"}
 for key in color:
   print(key)
```
c2
c1
c3

Following for loop iterates through its values :

```python
 color = {"c1": "Red", "c2": "Green", "c3": "Orange"}
 for value in color.values():
   print(value)
```

Green
Red
Orange

You can attach an optional else clause with for statement, in this case, syntax will be -
```python
for variable_name in sequence :
    statement_1 
    statement_2
    ....
else :
    statement_3 
    statement_4
    ....
```
The else clause is only executed after completing the for loop. If a break statement executes in first program block and terminates the loop then the else clause does not execute. 

## While loop

While loops are used to repeatedly execute a block of program statements. Here is the syntax.

Syntax:
```python
while (expression) :
    statement_1
    statement_2
    ....
```
The while loop runs as long as the expression (condition) evaluates to True and execute the program block. The condition is checked every time at the beginning of the loop and the first time when the expression evaluates to False, the loop stops without executing any remaining statement(s). The following example prints the digits 0 to 4 as we set the condition x < 5.

x = 0;
while (x < 5):
     print(x)
     x += 1



Output:

0
1
2
3
4

One thing we should remember that a while loop tests its condition before the body of the loop (block of program statements) is executed. If the initial test returns false, the body is not executed at all. For example the following code never prints out anything since before executing the condition evaluates to false.

x = 10;
while (x < 5):
     print(x)
     x += 1



Flowchart:
Python while loop

 

The following while loop is an infinite loop, using True as the condition:

x = 10;
while (True):
     print(x)
     x += 1



Flowchart:
Python while loop infinite

 
Python: while and else statement

There is a structural similarity between while and else statement. Both have a block of statement(s) which is only executed when the condition is true. The difference is that block belongs to if statement executes once whereas block belongs to while statement executes repeatedly.

You can attach an optional else clause with while statement, in this case, syntax will be -
while (expression) :
    statement_1
    statement_2
    ......
else :
    statement_3
    statement_4
    ......

The while loop repeatedly tests the expression (condition) and, if it is true, executes the first block of program statements. The else clause is only executed when the condition is false it may be the first time it is tested and will not execute if the loop breaks, or if an exception is raised. If a break statement executes in first program block and terminates the loop then the else clause does not execute. In the following example, while loop calculates the sum of the integers from 0 to 9 and after completing the loop, else statement executes.


x = 0;
s = 0
while (x < 10):
     s = s + x
     x = x + 1
else :
     print('The sum of first 9 integers : ',s)    



Output:

The sum of first 9 integers:  45

Flowchart:
Python while else loop

 
Example: while loop with if-else and break statement

x = 1;
s = 0
while (x < 10):
     s = s + x
     x = x + 1
     if (x == 5):
          break
else :
     print('The sum of first 9 integers : ',s)        
print('The sum of ',x,' numbers is :',s) 



Output:

The sum of  5  numbers is : 10

In the above example the loop is terminated when x becomes 5. Here we use break statement to terminate the while loop without completing it, therefore program control goes to outside the while - else structure and execute the next print statement. 

break statement

The break statement is used to exit a for or a while loop. The purpose of this statement is to end the execution of the loop (for or while) immediately and the program control goes to the statement after the last statement of the loop. If there is an optional else statement in while or for loop it skips the optional clause also. Here is the syntax.

Syntax:

 
			  while (expression1) :
     statement_1 
     statement_2
     ......
     if expression2 :
     break

for variable_name in sequence :
   statement_1 
   statement_2
   if expression3 :
     break

Example: break in for loop

In the following example for loop breaks when the count value is 5. The print statement after the for loop displays the sum of first 5 elements of the tuple numbers.

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
num_sum = 0
count = 0
for x in numbers:
    num_sum = num_sum + x
    count = count + 1 
    if count == 5:
        break
print("Sum of first ",count,"integers is: ", num_sum)



Output:

Sum of first  5 integers is:  15

Example: break in while loop

In the following example while loop breaks when the count value is 5. The print statement after the while loop displays the value of num_sum (i.e. 0+1+2+3+4).

num_sum = 0
count = 0
while(count<10):
    num_sum = num_sum + count
    count = count + 1 
    if count== 5:
        break
print("Sum of first ",count,"integers is: ", num_sum)



Output:

Sum of first  5 integers is :  10

continue statement

The continue statement is used in a while or for loop to take the control to the top of the loop without executing the rest statements inside the loop. Here is a simple example.

for x in range(7):
    if (x == 3 or x==6):
        continue
    print(x)



Output:

0
1
2
4
5

In the above example, the for loop prints all the numbers from 0 to 6 except 3 and 6 as the continue statement returns the control of the loop to the top

