<center>
<h1>Python Exam</h1>
</center>

0. בקוד נתון, מהי שגיאה:
```py
1name = input ("Please insert your name")
print (1name)

```
* a.רווח בין 'קלט' לבין סוגריים הוא שגיאה 
* b.רווח בין 'פלט' לבין סוגריים הוא שגיאה
* c.שם המשתנה מוגדר בצורה שגויה
* d.כל התשובות נכונות

1. בקוד נתון, מהי שגיאה:
```py
x=''
for x in "We Love Python":
    if x.isupper():
        print(x)
```
* a. איזו שגיאה? אין שגיאה בקוד
* b.x מוגדר, כך שהלולאה לא תעבוד  
* c.'isupper()'אין שיטה בפיתון
* d. פונקציית ההדפסה צריכה להיות רווח בינה לבין סוגריים

2. מה יהיה פלט של קטע קוד:
```py
for i in range(10):
    print(str(i) * i)
```
* a.
```bash
1 2 3 4 5 6 7 8 9
```
* b.
```bash
1 22 333 4444 55555 666666 7777777 88888888 999999999 
```
* c.
```bash
1
2
3
4
5
6
7
8
9
```
* d. 
```bash
1
22
333
4444
55555
666666
7777777
88888888
999999999 
```
3. מה יהיה פלט של קטע קוד:
```py
i = 1
while i < 6:
  print(i)
  i += 1
```
* a.
```py
1
2
3
4
5
```
* b.
```py
5
4
3
2
1
```
* c.
```py
1 2 3 4 5
```
* d. כל התשובות נכונות

4. כיצד לקרוא (לבצע) פונקציה בשם my_function.:
```py
def my_function():
  print("Hello from a function")
```
* a. פשוט תקראו לשמו: my function()
* b.אוקיי, אולי אם תשתמש בשמו: my_function (), זה יעבוד
* c.אינך יכול להשתמש בפונקציה מכיוון שהיא לא מוגדרת כראוי
* d. כל התשובות נכונות

5. בקוד נתון, מה יהיה הפלט:
```py
myTuple = ("John", "Peter", "Vicky")

x = ",".join(myTuple)

print(x) 
```
* a.הפלט יהיה John#Peter#Vicky
* b.הפלט יהיה John/Peter/Vicky
* c.הפלט יהיה John Peter Vicky
* d. הפלט יהיה John,Peter,Vicky

6. בקוד נתון, מה יעצור את הלולאה עם ערך שלו יהיה 3:
```py
i = 1
while i < 6:
  if i == 3:
      _______ #תשלימו כאן את הפקודה החסרה
  i += 1
```
* a.continue
* b.break
* c.pass
* d. כלום - צריך לחכות שלולאה תגיע לערך 6

7. בקוד נתון, מהי שגיאה:
```py
var = 6

while True:
  if var == 3:
    var +=1
  if var < 4:
    var -=1
  if var <= 2:
    break
  var -=1

```
מהי התשובה הכי מדוייקת:
* a. אין שגיאה - הכל תקיו, כשלולאה תגיע לערך קטן או שווה ל2 זה יעצור
* b. יש שגיאה - זה נתקע על ערך 4
* c. יש שגיאה - זה נתקע על ערך 3
* d. יש שגיאה - זה מעולם לא יגיע לערך שקטן או שווה ל2

8. בקוד נתון, מהי התוצאה:
```py
    print(1, 2, 3, 4, sep='*')
```
* a. 1 2 3 4
* b. 1234
* c. `1*2*3*4`
* d. 24

9. בקוד נתון, מהי התוצאה: 
```py
def printLine(text):
  print(text, 'is awesome.')

printLine('Python')
```
* a.Python
* b.Python is awesome.
* c.text is awesome.
* d.is awesome.