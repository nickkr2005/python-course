# UNIT 4

# EX 4.1.1
# 1. מתקבלת הודעת שגיאה מסוג IndentationError.
# 2. מתקבלת הודעת שגיאה מסוג SyntaxError.
# 3. מודפס "?What is the temperature".



# EX 4.2.1
# 1. זהה
# 2. שונה
# 3. זהה


# EX 4.2.2
str = input("Enter a word: ")
if str == str[::-1]:
    print("OK")
else:
    print("NOT")


# EX 4.2.3
str = input("Insert the temperature you would like to convert: ")
if str[-1] == 'c':
    print(f"{int((9*int(str[:-1])+32*5)/5)}f")
if str[-1] == 'C':
    print(f"{int((9*int(str[:-1])+32*5)/5)}F")
elif str[-1] == 'f':
    print(f"{int((5*int(str[:-1])-160)/9)}f")
elif str[-1] == 'F':
    print(f"{int((5*int(str[:-1])-160)/9)}C")


# EX 4.2.4
import calendar

date = input("Enter a date: ").split("/")
print(calendar.day_name[calendar.weekday(int(date[2]),int(date[1]),int(date[0]))])



# EX 4.3.1
ch = input("Please enter a word: ")

if len(ch)>1 and not ch.isalpha():
    print("E3")
elif len(ch)>1:
    print("E1")
elif not ch.isalpha():
    print("E2")
else:
    print(ch.lower())
