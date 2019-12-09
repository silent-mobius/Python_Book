'''
תגדירו רשימה חדשה בשם פירות
תבקשו ממשתמש שיכניס פירות לתוך רשמה עד שיהיו 7 פירות ברשימה
אם ערך של פרי מסוים חוזר על עצמו יותר מפעם אחת, אסור להכניס אותו
לרשימה קיימת ויש צורך להוציא למשתמש הודעת שגיאה אבל בכל זאת להמשיך להריץ את התוכנה
'''

fruits = []

while len(fruits) < 7:
    fruit = input("Please enter fruit: ")
    if fruit in fruits:
        print(fruit, " is already in list, please try again")
        continue
    else:
        fruits.append(fruit)

print(len(fruits), fruits)