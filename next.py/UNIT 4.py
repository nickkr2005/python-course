# UNIT 4


# EX 4.1.1
# 4.5


# EX 4.1.2
def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    return ' '.join((words[word] for word in sentence.split(" ")))


# EX 4.1.3
def first_prime_over(n):
    return next(i for i in range(n,n**n) if is_prime(i))



# EX 4.2.1
# מבצעים פעולות במהירות


# EX 4.2.2
def parse_ranges(ranges_string):
    ranges = ranges_string.split(',')
    numbers = []
    for r in ranges:
        start, end = map(int, r.split('-'))
        generator = (x for x in range(start, end + 1))
        numbers.extend(generator)
    return numbers



# EX 4.3.1
# לקבל אליו ארגומנטים
# שילוב לולאת while
# עטיפת קטע קוד בבלוק try-except
# שימוש רב פעמי


# EX 4.3.2
# לא יודפס כלום למסך.


# EX 4.3.3
# המשתנים הלוקאליים בטווח ההכרה של הפונקציה נשמרים בין הקריאות לה
# הפונקציה מאפשרת להפיק מספר רב של ערכים


# EX 4.3.4
def get_fibo():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b



# EX 4.4
from itertools import islice

def gen_secs():
    sec = 0
    while sec < 60:
        yield sec
        sec+=1

def gen_minutes():
    min = 0
    while min < 60:
        yield min
        min+=1

def gen_hours():
    hour = 0
    while hour < 24:
        yield hour
        hour+=1

def gen_time():
    for hour in gen_hours():
        for min in gen_minutes():
            for sec in gen_secs():
                yield f"{hour}:{min}:{sec}"

def gen_years(start=2024):
    while True:
        yield start
        start+=1

def gen_months():
    mon = 1
    while mon<=12:
        yield mon
        mon+=1

def gen_days(month, leap_year=True):
    day = 1
    if month in [1,3,5,7,8,10,12]:
        days = 31
    elif month in [4,6,9,11]:
        days = 30
    elif leap_year:
        days = 29
    else:
        days = 28

    while day <= days:
        yield day
        day+=1

def gen_date():
    for year in gen_years():
        leap_year = year % 400 == 0 or year % 4 == 0 and year % 100 != 0
        for month in gen_months():
            for day in gen_days(month,leap_year):
                for time in gen_time():
                    yield f"{day}/{month}/{year} " + time

def main():
    date = gen_date()
    date_skip = next(islice(date, 1000000 , None))
    for i in range(10):
        print(date_skip)
        date_skip = next(islice(date, 1000000 , None))

if __name__ == "__main__":
    main()