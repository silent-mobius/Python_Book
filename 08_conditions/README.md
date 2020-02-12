# Python Operators, Conditions and If statements

## Python Arithmetic, Comparison and Logical Operators

### Arithmetic Operators

Operator | Name | Example | Result
------ | ------ | -------- | ------
+ | Addition | x+y | Sum of x and y.
- | Subtraction | x-y | Difference of x and y.
* | Multiplication | x*y | Product of x and y.
/ | Division | x/y | Quotient of x and y.
% | Modulus | x%y | Remainder of x divided by y.
** | Exponent | x**y | x**y will give x to the power y
// | Floor Division | x/ y | The division of operands where the result is the quotient in which the digits after the decimal point are removed.

These conditions can be used in several ways, most commonly in "if statements" and loops.

### Comparison Operators

Operator | Name | Example | Result
------ | ------ | -------- | ------
== | Equal | x==y | True if x is exactly equal to y.
!= | Not equal | x!=y | True if x is exactly not equal to y.
> | Greater than | x>y | True if x (left-hand argument) is greater than y (right-hand argument).
< | Less than | x<y | True if x (left-hand argument) is less than y (right-hand argument).
>= | Greater than or equal to | x>=y | True if x (left-hand argument) is greater than or equal to y (left-hand argument).
<= | Less than or equal to | x<=y | True if x (left-hand argument) is less than or equal to y (right-hand argument).

### Logical Operators

Operator | Example | Result
------ | ------ | ------
and | (x and y) | is True if both x and y are true.
or | (x or y) | is True if either x or y is true.
not | (x not y) | If a condition is true then Logical not operator will make false.

### Assignment Operators

Operator | Shorthand | Expression | Description
------ | ------ | -------- | ------
+= | x+=y | x = x + y | Adds 2 numbers and assigns the result to left operand.
-= | x-= y | x = x -y | Subtracts 2 numbers and assigns the result to left operand.
*= |x*= y | x = x*y | Multiplies 2 numbers and assigns the result to left operand.
/= | x/= y | x = x/y | Divides 2 numbers and assigns the result to left operand.
%= | x%= y | x = x%y | Computes the modulus of 2 numbers and assigns the result to left operand.
**= | x**=y | x = x**y | Performs exponential (power) calculation on operators and assign value to the equivalent to left operand.
//= | x//=y | x = x//y | Performs floor division on operators and assign value to the left operand.

## Conditional Operators

Conditional expressions or ternary operator have the lowest priority of all Python operations. The expression x if C else y first evaluates the condition, C (not x); if C is true, x is evaluated and its value is returned; otherwise, y is evaluated and its value is returned.

## if..elif..else

The if-elif-else statement is used to conditionally execute a statement or a block of statements. Conditions can be true or false, execute one thing when the condition is true, something else when the condition is false

if statement

The Python if statement is same as it is with other programming languages. It executes a set of statements conditionally, based on the value of a logical expression.

Syntax:
```python
if expression :
    statement_1 
    statement_2
    ....

```

In the above case, expression specifies the conditions which are based on Boolean expression. When a Boolean expression is evaluated it produces either a value of true or false. If the expression evaluates true the same amount of indented statement(s) following if will be executed. This group of the statement(s) is called a block

### if .. else statement

In Python if .. else statement, if has two blocks, one following the expression and other following the else clause. Here is the syntax.

Syntax:

```python
    if expression :
        statement_1
        statement_2
        ....
    else : 
        statement_3 
        statement_4
        ....
```

In the above case if the expression evaluates to true the same amount of indented statements(s) following if will be executed and if the expression evaluates to false the same amount of indented statements(s) following else will be executed. See the following example. The program will print the second print statement as the value of a is 10.

```python
a=10
if(a>10):
    print("Value of a is greater than 10")
else :
    print("Value of a is 10")
```

### if .. elif .. else statement

Sometimes a situation arises when there are several conditions. To handle the situation Python allows adding any number of elif clause after an if and before an else clause. Here is the syntax.

Syntax:

```python
if expression1 :
         statement_1
         statement_2
         ....
   elif expression2 :
     statement_3
     statement_4
     ....
   elif expression3 :
     statement_5
     statement_6
     ....................
   else :
     statement_7
     statement_8
```

In the above case Python evaluates each expression (i.e. the condition) one by one and if a true condition is found the statement(s) block under that expression will be executed. If no true condition is found the statement(s) block under else will be executed. In the following example, we have applied if, series of elif and else to get the type of a variable.

```python
var1 = 1+2j
if (type(var1) == int):
    print("Type of the variable is Integer")
elif (type(var1) == float):
    print("Type of the variable is Float")
elif (type(var1) == complex):
    print("Type of the variable is Complex")
elif (type(var1) == bool):
    print("Type of the variable is Bool")
elif (type(var1) == str):
    print("Type of the variable is String")
elif (type(var1) == tuple):
    print("Type of the variable is Tuple")
elif (type(var1) == dict):
    print("Type of the variable is Dictionaries")
elif (type(var1) == list):
    print("Type of the variable is List")
else:
    print("Type of the variable is Unknown")
```

Output:

> Type of the variable is Complex

### Nested if .. else statement

In general nested if-else statement is used when we want to check more than one conditions. Conditions are executed from top to bottom and check each condition whether it evaluates to true or not. If a true condition is found the statement(s) block associated with the condition executes otherwise it goes to next condition. Here is the syntax :

Syntax:

 
     if expression1 :
         if expression2 :
          statement_3
          statement_4
        ....
      else :
         statement_5
         statement_6
        ....
     else :
	   statement_7 
       statement_8

In the above syntax expression1 is checked first, if it evaluates to true then the program control goes to next if - else part otherwise it goes to the last else statement and executes statement_7, statement_8 etc.. Within the if - else if expression2 evaluates true then statement_3, statement_4 will execute otherwise statement_5, statement_6 will execute. See the following example.

age = 38
if (age >= 11):
  print ("You are eligible to see the Football match.")
  if (age <= 20 or age >= 60):
      print("Ticket price is $12")
  else:
      print("Tic kit price is $20")
else:
    print ("You're not eligible to buy a ticket.")

Output :

>You are eligible to see the Football match.
>Tic kit price is $20

In the above example age is set to 38, therefore the first expression (age >= 11) evaluates to True and the associated print statement prints the string "You are eligible to see the Football match". There after program control goes to next if statement and the condition ( 38 is outside <=20 or >=60) is matched and prints "Tic ket price is $12".


[back to top](#arithmetic-operators)
Or
[back to main](../README.md)