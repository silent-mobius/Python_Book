# Full Python Exam

## Variables and slicing  משתנים וחיתוך משתנים
1.
- נתונים משתמנים
  - var = ('abc','dfg',([1,2,3],[4,6,7],[9,8,7]),('ab'),('bc'))
  - עליכם\ן לחתוך משתנים נתונים ולשמור במשתנים זמניים או להסביר למה לא ניתן לחתוך אותם
```py
# with slices
```
  -  איך יראה הקוד שלפיו ניתן להדפיס את הערך 7 מתוך רשימה[4,6,7]
```py
var[2][1][2]
```
  - האם ניתן להמיר את הערכים של טופל לרשימה בתוך משתנה ? הסבר
```py
#yes
var[2][1][2]=11
```

2.
- עלייך לכתוב קוד פייתון לפי ההוראות הבאות: 
  -  תכריז על משתנה מסוג רשימה בשם users
  -  תוסיפו לרשימה ריקה שמות הבאים : "Karen", "Michael", "Jordan"
  -  תמחקו את משתמש האחרון מהרשימה (הכוונה את ג'ורדן)
  -  תהפכו סדר של המשתמשים ברשימה
  -  הכניסו את שם 'Alex' בתוך הרשימה  במיקום 1
  -  תגדילו את הרשימה עם משמתמשים: 'me', 'myself', 'Irene'
  -  תחתכו את רשימה ממיקום 0 עד 2 ותשמרו במשתנה חדש

```py
users=[]
users.append('Karen')
users.append('Michael')
users.append('Jordan')
users.pop() #users.remove(2)
users.reverse()
users.insert(1,'Alex')
users = users + ['me', 'myself', 'Irene']
new_users = users[0:2]
```

## Conditions and loops  תנאים ולולאות
3.
- נתון קוד:
```py
value = int(input("Enter an integer value: "))
if value % 5 = 0 and value % 3 = 0:
print("FizzBuzz")
elif value % 3 = 0:
print("Fizz")
elif value % 5 = 0:
print("Buzz")
else:
print(value)
```
 - יש תקלות בקוד - אנא תתקנו אותם
```py
value = int(input("Enter an integer value: "))
if value % 5 == 0 and value % 3 == 0:
    print("FizzBuzz")
elif value % 3 == 0:
    print("Fizz")
elif value % 5 == 0:
    print("Buzz")
else:
    print(value)
```
 - מה יקרה אם יכניסו ערך 6 לקוד ? 
 ```py
#Fizz
 ```
 - מה יקרה עם יכניסו ערך 15 לקוד ?
 ```py
#FizzBuzz
 ```

## Functions  פונקציות
4.
-  כתוב פונקציה בשם  split_name 
   - שלוקח מחרוזת ומחזירה מילון עם שם פרטי ושם משפחה אחרון
   - ודא שפונקציה יכולה להתמודד עם שמות משפחה רב-מילוליים

5.
- כתוב פונקציה `is_palindrome` 
  - ( כדי לבדוק אם מחרוזת היא פלינדרום (קורא אותו  הדבר משמאל לימין ומימין לשמאל




