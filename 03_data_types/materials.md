# Python Data Types

###  Built-in Data Types

In programming, data type is an important concept.
Variables can store data of different types, and different types can do different things.
Python has the following data types built-in by default, in these categories:

Type | Value
------------ | -------------
Text | 	str
Numeric| 	int, float, complex
Sequence| 	list, tuple, range
Mapping | 	dict
Set | 	set, frozenset
Boolean | 	bool
Binary| 	bytes,bytearray

### Getting the Data Type

You can get the data type of any object by using the type() function:

Print the data type of the variable x:

```python3
x = 5
print(type(x))
```

### Setting the Data Type

In Python, the data type is set when you assign a value to a variable:

```python3
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
```

### Setting the Specific Data Type

If you want to specify the data type, you can use the following constructor functions:

```python3
x = str("Hello World") 	str 	
x = int(20) 	int 	
x = float(20.5) 	float 	
x = complex(1j) 	complex 	
x = list(("apple", "banana", "cherry")) 	list 	
x = tuple(("apple", "banana", "cherry")) 	tuple 	
x = range(6) 	range 	
x = dict(name="John", age=36) 	dict 	
x = set(("apple", "banana", "cherry")) 	set 	
x = frozenset(("apple", "banana", "cherry")) 	frozenset 	
x = bool(5) 	bool 	
x = bytes(5) 	bytes 	
x = bytearray(5) 	bytearray 	
x = memoryview(bytes(5)) 	memoryview 	
```

---

### Python Numbers

There are three numeric types in Python:

* int
* float
<!--*    complex #We are not going to dive in this too deep -->
Variables of numeric types are created when you assign a value to them:

```python3
x = 1    # int
y = 2.8  # float
```
<!-- z = 1j   # complex -->

To verify the type of any object in Python, use the type() function:

```python3
print(type(x))
print(type(y))
print(type(z))
```

#### Int

Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

Integers:

```python3
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
```

##### Float

Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

Floats:

```python3
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
```

Float can also be scientific numbers with an "e" to indicate the power of 10.

Floats:

```python3
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
```
<!--
Complex

Complex numbers are written with a "j" as the imaginary part:


Complex:
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
Type Conversion

You can convert from one type to another with the int(), float(), and complex() methods:
-->

Convert from one type to another:

```python3
x = 1 # int
y = 2.8 # float
```

<! --z = 1j # complex -->

> convert from int to float:
  > a = float(x)


> convert from float to int:
  > b = int(y)

<!--
#convert from int to complex:
c = complex(x)
-->

```python3
print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
```

> **Note: You cannot convert complex numbers into another number type.**
