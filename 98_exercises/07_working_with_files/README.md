# Working with files Exercises

###### **Note**: Make sure that you have Text Editor installed


## Create a folder named 07_working_with_files and save all the exercises below in it.

### Reading and Writing Files

#### Ex1.

Create a script that will ask you to insert a long string with letters, numbers and special characters:

- save the data to tmp file.
- loop through the inserted string:
  - if character is alpha create file named "chars" and write it in to it.
  - if character is number create file name "numbers" and write it in to it.
  - if character is special create file name "numbers" and write it in to it.


#### Ex2.

Create a script that will read through the latest log files in `/var/log` and print to user all alerts that have word error in them.

#### Ex3.

Create a script that reads `/etc/passwd` and copies its data to passwd_tmp file at `/tmp` folder

#### Ex4.

Create a file named names.txt. The file contains a list of names (first and last name). Each is in a separate row. Write a program that prints how many names there are in the file.

#### Ex5.

Create a file called number.txt that contains a series of integers and a space between them. Write a program that reads these numbers and prints their amount and their average.

#### Ex6.

Write a program that prints random numbers into a file called numbers.txt. Each random number is in the range of 1 to 500. The user determines how many such numbers should be printed to the file. To produce random numbers in the range of 1 to 500, record the following commands:

```py
import random
Random Rand (1,500)
```

#### Ex7.

Create a file called coffee.txt that contains coffee information from Wikipedia (copy information from Wikipedia into the file). A program address that prints several times the word coffee appears in the file.

#### Ex8.

Create a file named file1.txt that contains the following sentences:
```bash
Python is a great language.
I love python.
I thik Java is better.
When is the next python lesson? I simply can\'t miss it!
```
- Write a program that reads all rows to a list named list1 (each row will enter as a list into list1). Go through the list and remove all entries that do not have the word Python (regardless of upper or lower case).
- If you have to remove even one line, add this line to the file: This file is corrupted.

