# Python Exam

0.What does the following code do?
```py
    try:
      # code that can raise error
       pass
      
    except (TypeError, ZeroDivisionError):
      print("Two")
```
Choose one
* a.Prints Two if exception occurs (doesn’t matter which exception).
* b.Prints Two if exception doesn’t occur.
* c.Prints Two if TypeError or ZeroDivisionError exception occurs.
* d .Prints Two only if both TypeError and ZeroDivisionError exception occurs.

1.Which of the following statements is true?
Choose one
* a.Python is a high level programming language.
* b.Python is an interpreted language.
* c.Python is an object-oriented language.
* d.All of the above.

2.What is used to define a block of code (body of loop, function etc.) in Python?
Choose one
* a.Curly braces
* b.Parenthesis
* c.Indentation
* d.Quotation

3.What is the output of the following code?
```py
    if None:
        print(“Hello”)
```
Choose one
* a.False
* b.Hello
* c.Nothing will be printed
* d.Syntax error

4.What is the output of the following code?
```py
    for i in [1, 0]:
      print(i+1)
```
Choose one
* a. `
    2

    1
    `

* b. [2, 1]
	
* c. `
    2

    0
    `
* d. [2, 0]

5. Opening a file in ‘a’ mode
Choose one
* a.opens a file for reading
* b.opens a file for writing
* c.opens a file for appending at the end of the file
* d.opens a file for exclusive creation

6. What does the following code do?
```py
    f = open("test.txt")
```
Choose one
* a.Opens test.txt file for both reading and writing
* b.Opens test.txt file for reading only
* c.Opens test.txt file for writing only
* d.Opens test.txt file in god mode


7.Which of the following codes closes file automatically if exception occurs?
Choose one
* a.
```py
    with open("test.txt", encoding = 'utf-8') as f:
        # perform file operation
```
* b.
```py
    try:
         f = open("test.txt",encoding = 'utf-8')
         # perform file operations
    finally:
        f.close()
```
* c.None of the above
* d.Both of the above

8.For the following code,
```py
    f = open('test.txt', 'r', encoding = 'utf-8')
    f.read()
```
Which of the following statement is true?
Choose one
* a.This program reads the content of test.txt file.
* b.If test.txt contains newline, read() will return newline a ‘\n’.
* c.You can pass an integer to the read() method.
* d.All of the above.


9. What is the output of the following code?
```py
    number = 5.0
    try:
        r = 10/number
        print(r)
    except:
        print("Oops! Error occurred.")
```
Choose one
* a.Oops! Error occurred.
* b.2.0
* c.2.0 Oops! Error occurred.
* d.None object