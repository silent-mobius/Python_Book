# Python Syntax
---


Python syntax can be executed by writing directly in the Command Line: [img]

Or by creating a python file on the server, using the .py file extension, and running it in the Command Line: [img]

### REPL: Python Interpreter 
<!-- needs to have explanation-->
As mention in [previous chapter](../00_intro/README.md) python is interpreted language. The interpretation for this kind of projects is done in a manner of REPL.

Read–eval–print loop (REPL), also termed an interactive toplevel or language shell, is a simple, interactive computer programming environment that takes single user inputs (i.e., single expressions), evaluates (executes) them, and returns the result to the user.

In a REPL, the user enters one or more expressions (rather than an entire compilation unit) and the REPL evaluates them and displays the results. The name read–eval–print loop comes from the names of the Lisp primitive functions which implement this functionality:

The `read` function accepts an expression from the user, and parses it into a data structure in memory. For instance, the user may enter the s-expression (+ 1 2 3), which is parsed into a linked list containing four data elements.

The `eval` function takes this internal data structure and evaluates it. In Lisp, evaluating an s-expression beginning with the name of a function means calling that function on the arguments that make up the rest of the expression. So the function + is called on the arguments 1 2 3, providing (yielding) the result 6.

The `print` function takes the result provided (yielded) by eval, and prints it out to the user. If it is a complex expression, it may be pretty-printed to make it easier to understand.

The development environment then returns to the read state, creating a `loop`, which terminates when the program is closed. 

REPL's are interactive, by which i mean that they interact with the user by success, the command provided to REPL with work or by error, the command will `NOT` work. REPL usually looks same as command line, for example: 

- Open cmd/terminal of your OS
- Type in it `python3` command and you are in
- It should look like this:
  - ![](../.img/repl.png)
- In case you see  `python 2.7` instead of what you have in picture, then it means that you need to upgrade your current version of python to `python 3.6` or higher.

### Saving the code

Although running in REPL is fun and all, one must always run the list of commands from somewhere, mostly because it misses point of programming if you'll run all the commands manually. 

list of python (or any other high level language) commands that are saved in to the file is usually called as `code`.

To write code, we use a type of `text editor` to write and run it. There are many text editor on www, here is short list of ones that i'd suggest for this course:

- GEANY --> a lightweight IDE for general purpose of development.
  - ![GEANY](../.img/geany.png) 
- ATOM --> a extencible text editor with bunch tools that can be added.
  - ![ATOM](../.img/atom.png) 
- VSCODIUM --> a clone project of atom and vscode with more native OpenSource licensing and agenda.
  - ![VSCODIUM](../.img/vscode.png) 


### Python Indentation

Indentation refers to the spaces at the beginning of a code line.
Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.
Python uses indentation to indicate a block of code.
```py
if 5 > 2:
    print("Five is greater than two!")      #<-- 4 space indentation
```
Python will give you an error if you skip the indentation:

```py
if 5 > 2:
print("Five is greater than two!")  #<-- NO INDENTATION
```


### Python Variables

In Python variables are created the moment you assign a value to it:
```py
x = 5
y = "Hello, World!
```
Python has no command for declaring a variable.
Unlike other programming languages, Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.


### Comments

Comments can be used to explain Python code.

Comments can be used to make the code more readable.

Comments can be used to prevent execution when testing code.
Creating a Comment

Comments starts with a #, and Python will ignore them:

```py
#This is a comment
print("Hello, World!")
```
Comments can be placed at the end of a line, and Python will ignore the rest of the line:

```py
print("Hello, World!") #This is a comment
```
Comments does not have to be text to explain the code, it can also be used to prevent Python from executing code:

```py
#print("Hello, World!")
print("Cheers, Mate!")
```
### Multi Line Comments

Python does not really have a syntax for multi line comments.

To add a multiline comment you could insert a # for each line:

```py
#This is a comment
#written in
#more than just one line
print("Hello, World!")

```

Or, not quite as intended, you can use a multiline string.
Since Python will ignore string literals that are not assigned to a variable, you can add a multiline string (triple quotes) in your code, and place your comment inside it:
```py
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")
```
As long as the string is not assigned to a variable, Python will read the code, but then ignore it, and you have made a multiline comment.
