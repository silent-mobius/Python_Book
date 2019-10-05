#!/usr/bin/env python3

x = 5
print(type(x))

x = "Hello World" #	str 	
x = 20 	#int 	
x = 20.5 	#float 	 	
x = ["apple", "banana", "cherry"] 	#list 	
x = ("apple", "banana", "cherry") 	#tuple 	
x = range(6) 	#range 	
x = {"name" : "John", "age" : 36} 	#dict 	
x = {"apple", "banana", "cherry"} 	#set 	
x = frozenset({"apple", "banana", "cherry"}) 	#frozenset 	
x = True 	#bool 	
x = b"Hello" 	#bytes 	
x = bytearray(5) 	#bytearray 	
x = memoryview(bytes(5)) 	#memoryview 

x = str("Hello World") 	#str 	
x = int(20) 	#int 	
x = float(20.5) 	#float 	
x = complex(1j) 	#complex 	
x = list(("apple", "banana", "cherry"))  #list 	
x = tuple(("apple", "banana", "cherry")) 	#tuple 	
x = range(6) 	#range 	
x = dict(name="John", age=36) 	#dict 	
x = set(("apple", "banana", "cherry")) 	#set 	
x = frozenset(("apple", "banana", "cherry")) 	#frozenset 	
x = bool(5) 	#bool 	
x = bytes(5) 	#bytes 	
x = bytearray(5) 	#bytearray 	
x = memoryview(bytes(5)) 	#memoryview 	


x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))


x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))


# all of the following are equivalent
my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

my_string = '''Hello'''
print(my_string)

# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)


str = 'programiz'
print('str = ', str)

#first character
print('str[0] = ', str[0])

#last character
print('str[-1] = ', str[-1])

#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])

#slicing 6th to 2nd last character
print('str[5:-2] = ', str[5:-2])


# index must be in range
>>> my_string[15]  
...IndexError: string index out of range
# index must be an integer
>>> my_string[1.5] 
...TypeError: string indices must be integers
...TypeError: 'str' object doesn't support item deletion
>>> del my_string
>>> my_string
...NameError: name 'my_string' is not defined



str1 = 'Hello'
str2 ='World!'

# using +
print('str1 + str2 = ', str1 + str2)

# using *
print('str1 * 3 =', str1 * 3)


>>> 'Hello ''World!'
'Hello World!'
>>> # using parentheses
>>> s = ('Hello '
...      'World')
>>> s
'Hello World'


count = 0
for letter in 'Hello World':
    if(letter == 'l'):
        count += 1
print(count,'letters found')


>>> 'a' in 'program'
True
>>> 'at' not in 'battle'
False




str = 'cold'

# enumerate()
list_enumerate = list(enumerate(str))
print('list(enumerate(str) = ', list_enumerate)

#character count
print('len(str) = ', len(str))


>>> print("He said, "What's there?"")
...SyntaxError: invalid syntax
>>> print('He said, "What's there?"')
...SyntaxError: invalid syntax



# using triple quotes
print('''He said, "What's there?"''')

# escaping single quotes
print('He said, "What\'s there?"')

# escaping double quotes
print("He said, \"What's there?\"")


>>> print("\\")
\
>>> print("This is printed\nin two lines")
This is printed
in two lines
>>> print("This is \x48\x45\x58 representation")
This is HEX representation


>>> print("This is \x41 \ngood example")
This is A
good example
>>> print(r"This is \x41 \ngood example")
This is \x41 \ngood example


# default(implicit) order
default_order = "{}, {} and {}".format('John','Bill','Sean')
print('\n--- Default Order ---')
print(default_order)

# order using positional argument
positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
print('\n--- Positional Order ---')
print(positional_order)

# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
print('\n--- Keyword Order ---')
print(keyword_order)



>>> # formatting integers
>>> "Binary representation of {0} is {0:b}".format(12)
'Binary representation of 12 is 1100'
>>> # formatting floats
>>> "Exponent representation: {0:e}".format(1566.345)
'Exponent representation: 1.566345e+03'
>>> # round off
>>> "One third is: {0:.3f}".format(1/3)
'One third is: 0.333'
>>> # string alignment
>>> "|{:<10}|{:^10}|{:>10}|".format('butter','bread','ham')
'|butter    |  bread   |       ham|'



>>> x = 12.3456789
>>> print('The value of x is %3.2f' %x)
The value of x is 12.35
>>> print('The value of x is %3.4f' %x)
The value of x is 12.3457


>>> "PrOgRaMiZ".lower()
'programiz'
>>> "PrOgRaMiZ".upper()
'PROGRAMIZ'
>>> "This will split all words into a list".split()
['This', 'will', 'split', 'all', 'words', 'into', 'a', 'list']
>>> ' '.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string'])
'This will join all words into a string'
>>> 'Happy New Year'.find('ew')
7
>>> 'Happy New Year'.replace('Happy','Brilliant')
'Brilliant New Year'


# empty list
my_list = []
# list of integers
my_list = [1, 2, 3]
# list with mixed datatypes
my_list = [1, "Hello", 3.4]


# nested list
my_list = ["mouse", [8, 4, 6], ['a']]


my_list = ['p','r','o','b','e']
# Output: p
print(my_list[0])
# Output: o
print(my_list[2])
# Output: e
print(my_list[4])
# Error! Only integer can be used for indexing
# my_list[4.0]
# Nested List
n_list = ["Happy", [2,0,1,5]]
# Nested indexing
# Output: a
print(n_list[0][1])    
# Output: 5
print(n_list[1][3])


my_list = ['p','r','o','b','e']
# Output: e
print(my_list[-1])
# Output: p
print(my_list[-5])



my_list = ['p','y','t','h','o','n',' ','c','o','u','r','s','e']
# elements 3rd to 5th
print(my_list[2:5])
# elements beginning to 4th
print(my_list[:-5])
# elements 6th to end
print(my_list[5:])
# elements beginning to end
print(my_list[:])


# mistake values
odd = [2, 4, 6, 8]
# change the 1st item
odd[0] = 1
# Output: [1, 4, 6, 8]
print(odd)
# change 2nd to 4th items
odd[1:4] = [3, 5, 7]  
# Output: [1, 3, 5, 7]
print(odd)

odd = [1, 3, 5]
odd.append(7)
# Output: [1, 3, 5, 7]
print(odd)
odd.extend([9, 11, 13])
# Output: [1, 3, 5, 7, 9, 11, 13]
print(odd)


