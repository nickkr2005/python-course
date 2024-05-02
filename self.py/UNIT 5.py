# UNIT 5


# EX 5.5.1
# A: המשתנה index הוא פרמטר של הפונקציה mystery.
# D: הערך 3 הוא ארגומנט שמועבר לפונקציה func.
# mystery :E ו-func מצביעות לאותו מקום בזיכרון המחשב.
# G: הפלט מהרצת קטע קוד מספר 3 (לאחר קטע קוד מספר 1) הוא zzzzzz.
# H: הקריאה לפונקציה mystery מתבצעת בקטע קוד מספר 2.



# EX 5.2.1
# 1. יודפס 1 ואז 1
# 2. יודפס 2 ואז 1
# 3. תודפס הודעת שגיאה
# 4.  יודפס 2 ואז 2 



# EX 5.3.1
# B: remainder(9, 8, True)
# F: remainder(9)


# EX 5.3.2
# def square_equation(a=1, b=0, c=0):
# def square_equation(a, b=0, c=0):


# EX 5.3.3
# 1. מודפס 17 / 12 / 15.
# 2. מודפס 17 / 15 / 12.
# 3. מודפס 17 / 12 / 17.
# 4. מתקבלת הודעת שגיאה מסוג TypeError.


# EX 5.3.4
def last_early(my_str):
    return my_str[-1].lower() in my_str[:-1].lower()


# EX 5.3.5
def distance(num1, num2, num3):
    return abs(num1-num2) == 1 and abs(num1-num3) >= 2 or abs(num1-num2) >= 2 and abs(num1-num3) == 1


# EX 5.3.6
def filter_teens(a=13, b=13, c=13):
    return fix_age(a) + fix_age(b) + fix_age(c)

def fix_age(age):
    if age>=13 and age<=19 and age!=15 and age!=16:
        age=0
    return age


# EX 5.3.7
def chocolate_maker(small, big, x):
    return x % 5 <= small and x % 5 + 5 * big >= x



# EX 5.4.1
def func(num1, num2):
    """Calculates a the letter represented by sum of two numbers.
    :param num1: added item1
    :param num2: added item2
    :type num1: int
    :type num2: int
    :return: The letter represented by the sum of num1 and num2
    :rtype: char
    """
    return chr(num1+num2)


def main():
    help(func)

if __name__ == "__main__":
    main()



# EX 5.5.1
def is_valid_input(letter_guessed):
    return len(letter_guessed)==1 and letter_guessed.isalpha()