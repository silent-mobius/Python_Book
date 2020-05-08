# Exception Exercises

###### **Note**: Make sure that you have Text Editor installed


#### Ex 1.
Write a program that receives user numbers in the loop and for each received number prints its root. Alert the user if they enter a non-number value, or enter a negative number.

#### Ex 2.
Write a program that receives a file name at the command line and prints the number of lines in the file. If the file does not exist, an appropriate message must be printed for the user. Here's what a sample session of the program looks like:

```bash
python3 script.py / etc / shells
11

python3 script.py / foo / bar
Sorry, file / foo / bar not found
```
#### Ex3.
The following code assumes a class called ImageFile that represents an image file. Write the class so that only files with the appropriate extension can be created and the following test passes:

```py
import unittest

class TestImageFile (unittest.TestCase):
     def test_good_ext (self):
         try:
             img = ImageFile ("file.png")
         except InvalidImageExt:
             self.fail ("png should be a valid file extension")

     def test_bad_ext (self):
         with self.assertRaises (InvalidImageExt):
             img = ImageFile ("file.mp3")

unittest.main ()
```
#### Ex 4. 