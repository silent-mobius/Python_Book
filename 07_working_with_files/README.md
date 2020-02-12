# Working with files

Does not matter what type of  work you are doing, with python, or any other programming language, working with files, is a valuable task.

Luckily, Python has few functions for creating, reading, updating, and deleting files, that do not need to many parameters to be passed.(No pointers and no file descriptors)

## File Handling

The first and probably most important function for working with files in Python is the `open()` function.

The `open()` function takes two parameters; `filename`, and `mode`(e.g. how you wish your file to be opened).

There are four different methods (modes) for opening a file:

type | what it stands for | explanations
--- |  ----------------- | --------------------
"r" | Read | Default value. Opens a file for reading, error if the file does not exist
"a" | Append | Opens a file for appending, creates the file if it does not exist
"w" | Write |Opens a file for writing, creates the file if it does not exist
"x" | Create | Creates the specified file, returns an error if the file exists


In addition you can specify if the file should be handled as binary or text mode

type | what it stands for | explanations
--- |  ----------------- | --------------------
"t" | Text | Default value. Text mode
"b" | Binary | Binary mode (e.g. images, pcaps,)

### Syntax

To open a file for reading it is enough to specify the name of the file:

```py
f = open("data.txt")
```
The code above is the same as:
```py
f = open("data.txt", "rt")
```
Because "r" for read, and "t" for text are the default values, you do not need to specify them.

> *_> *_Note_*_*: Make sure the file exists, or else you will get an error.


### Open a File

Assume we have the following file, located in the same folder as Python:

```txt

Hello! Welcome to imaginary world of python programming

If you are reading this, then it means, that file is open.

Good Luck!

Never Give Up Your Dreams!!!

We Cheer for you!!!
```
To open the file, use the built-in `open()` function.

The `open()` function returns a file object, which has a `read()` method for reading the content of the file:

```py
f = open("data.txt", "r")
print(f.`read()`)
```
### Read Only Parts of the File

By default the `read()` method returns the whole text, but you can also specify how many characters you want to return.
Return the `5 first characters` of the file:
```py
f = open("data.txt", "r")
print(f.read(5))
```
### Read Lines

You can return one line by using the readline() method:


Read one line of the file:
```py
f = open("data.txt", "r")
print(f.readline())
```
By calling readline() two times, you can read the two first lines:


Read two lines of the file:
f = open("data.txt", "r")
print(f.readline())
print(f.readline())

By looping through the lines of the file, you can read the whole file, line by line:


Loop through the file line by line:
f = open("data.txt", "r")
for x in f:
  print(x)
Close Files

It is a good practice to always close the file when you are done with it.


Close the file when you are finish with it:
f = open("data.txt", "r")
print(f.readline())
f.close()

> *_> *_Note_*_*: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.


Write to an Existing File

To write to an existing file, you must add `a` or `w` parameters to the `open()` function, but once that is done  you also need to use [Object Method](object) to write data to file. 

type | what it stands for | explanations
--- |  ----------------- | --------------------
"a" | Append | will append to the end of the file
"w" | Write |will overwrite any existing content


Open the file "data2.txt" and append content to the file:
```py
f = open("data2.txt", "a")
f.write("Now the file has more content!")
f.close()
#open and read the file after the appending:
f = open("data2.txt", "r")
print(f.read())
```

Open the file "data3.txt" and overwrite the content:
```py
f = open("data3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("data3.txt", "r")
print(f.read())
```
> *_Note_*: the "w" method will overwrite the entire file.

> `**Object Method**` : I know i just dropped a name bomb on you and then continued like nothing happend


## Create a New File

Just like before, to create a new files in Python, use the `open()` method, with one of the following parameters:


type | what it stands for | explanations
--- |  ----------------- | --------------------
"x" | Create | will create a file, returns an error if the file exist
"a" | Append | will create a file if the specified file does not exist
"w" | Write  | will create a file if the specified file does not exist


Create a file called "myfile.txt":
```py
f = open("myfile.txt", "x")
```
Result: a new empty file is created!


Create a new file if it does not exist:
```py
f = open("myfile.txt", "w")
```
## Delete a File

To delete a file, you must import the OS module, and run its os.remove() function:


Remove the file "data.txt":
```py
import os
os.remove("data.txt")
Check if File exist:
```
To avoid getting an error, you might want to check if the file exists before you try to delete it:


Check if file exists, then delete it:
```py
import os
if os.path.exists("data.txt"):
  os.remove("data.txt")
else:
  print("The file does not exist")
```

## Delete Folder

To delete an entire folder, use the os.rmdir() method:

Remove the folder "myfolder":
```py
import os
os.rmdir("myfolder")
```
> *_Note_*: You can only remove empty folders.


[back to top](#python-syntax)
Or
[back to main](../README.md)