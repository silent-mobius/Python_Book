<center>

# Python Exam

</center>

## הוראות מבחן

- הינכם נמצאים במבחן במבוא לתכנות בעזרת שפת פייתון 
- אתם\ן מחוייבים לענות על השאלות
- חלק מהשאלות יהיו הינם שאלות בנוסח אמריקאי
  - על מנת לשעות עליהם ,אתם\ן מחוייבים לשלוח את מספר שאלה ואת התשובה על השאלה למרצה למייל אשר מופיע על לוח
  - לוגמא תשובה לשאלה 5 תופיע יחד עם תשובה כך :
    - `C\5`
  - במבחן ישנו גם שאלות פתוחות  
  - במבחן ישנו גם שאלות עם טבלת מעקב
  - את התשובות לשאלות פתוחות צריך לשלוח למייל אשר רשום על הלוח
  - את טבלת מעקב צריך להעתיק אל קובץ אקסל ולמלא את התוצאות המעקב
    - את הקובץ צריך לצרף למייל.
  - **__אל לכם להשתמש באינטרנט על מנת לענות על השאלות פתוחות או שאלות בנוסח אמריקאי__**

---

0. בקוד נתון, יש תקלות קוד - אנא תקנו את הקוד:

```py
data=['ACME',50,91.1,(144,25,78)]

def get_tuple_middle_element_from_list(list):
for element in list:
        if type(element) is tuple:
                print(e[2])


get_taple_middle_element_from_list[dat]

```
<!-- 
 def get_tuple_middle_element_from_list(list):
    ...:     for element in list:
    ...:         if type(element) is tuple:
    ...:             print(element[1])
-->

1. בקוד נתון, יש תקלות קוד - אנא תקנו את הקוד

```py
data = []
v = ' '

def get_data_from_user():
    lst = []
    line = ' '
    print("To exit input loop type 999")
    while line != '999':
        line = input("Please insert integer >> ")
        if line == '999':
            break
        elif len(line) > 1:
            continue
        else: 
            lst.append(line)
    return lst


def print_ascii_value_of_element(lst):
    tmp = []
    for i in lst:
        if  str.isalpha(i):
            pass
        else:
            tmp.append(ord(i))
    return tmp

if len(data) == 0:
    data = get_data_from_user()

v = print_ascii_value_of_element(data) 

print(v)

```

2.מה תהיה תוצאה של הקוד הבא:
  - .ראה מטה

```py
def printValues():
    lst = list()
    for element in range(1,6):
        lst.append(element**2)
    print(lst)


printValues()
```
  - הסבר ופרט בעזרת טבלת מעקב הבאה


no:| element  | lst
--| -- | --
1 |    |
2 |    |
3 |    |
4 |    |
5 |    |


3. מה תהיה תוצאה של הקוד הבא
   -  .ראה מטה
```py

def second_largest(numbers):
  if (len(numbers)<2):
    return 
  if ((len(numbers)==2)  and (numbers[0] == numbers[1]) ):
    return
  dup_items = set()
  uniq_items = []
  for x in numbers:
    if x not in dup_items:
      uniq_items.append(x)
      dup_items.add(x)
  uniq_items.sort()
  return  uniq_items[-2]  

print(second_largest([1, 1, 1, 0, 0, 0, 2, -2, -2]))


```

   - הסבר ופרט בעזרת טבלת מעקב הבאה

no: |  numbers | dup_items | uniq_items | x
--- | -------- | --------- | ---------- | --
1| | | |
2| | | |
3| | | |
4| | | |
5| | | |
6| | | |
7| | | |
8| | | |
9| | | |


---

## שאלות בנוסח אמקריקאי

4. מה התוצאה של הקטע קוד הבא:

```py
tab = {1: 'python', 2: 'dev', 3 : 'week' , 4: 'is' , 5:'coming' } 
print(' {0[1]:s} {0[2]:s} {0[3]:s} {0[4]:s} {0[5]:s}'.format(tab)) 
```

- a.1 2 3 4
- b. 4 3 2 1
- c.python dev week is coming
- d.coming is week dev python

5. מה התוצאה של הקטע קוד הבא :

```py
def printinfo( name='Bruce', age=54 ):
   '''This prints a passed info into this function'''
   print("Name: ", name, "Age: ", age)
   return;

printinfo( age=5, name="Lily" )

```

- a. Bruce, 54
- b. 54, bruce
- c. 5, lily
- d. Lily, 5


6. מה התוצאה של הקטע קוד הבא:

```py
with open("test.txt",'w') as f:
    f.write("my first file\n")
    f.write("This file\n\n")
    f.write("contains three lines\n")
```

- a. יש תוצאה, כי תוכן נכתב לקובץ בשם test.txt
- b. יש תוצאה, כי תוכן מצורף לקובץ בשם test.txt 
- c. אין תוצאה, כי תוכן לא מצורף לקובץ בשם test.txt
- d. אין תוצאה, כי יש טעות בקוד

7. מה התוצאה של הקטע קוד הבא :

```py
my_list = ["mouse", [8, 4, 6], ['a']]

my_list[1][1]
```

- a. 1, 2
- b. 4
- c.[8,4,6]
- d. a

8. מה התוצאה של הקטע קוד הבא :

```py
data=[[1,2],[3,4],[5,6],[7,8],[9,0]]

for d in data:
    print(d[1])

```

- a. 1,3,5,7,8
- b. 1,2,3,4,5,6,7,8,9,0
- c. 2,4,6,8,0
- d. 1,3,5,7,9


9. מה מדוייק יותר מבין הגדרות הבאות:

- a. פקודת print() תדפיס תוכן של משנה ותרד לשורה חדשה
- b. פקודת len() ארוך של משתנה מסוג רשימה, רשימה שמורה,רשימה מיוחדת ומחזורת
- c. פקודת type() תדפיס את סוג המשתנה שהוא מקבל בסוגריים
- d. כל התשובות נכונות