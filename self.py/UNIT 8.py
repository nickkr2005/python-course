# UNIT 8



# EX 8.8.1
# 1. (2,3)
# 2. 2 than 3
# 3. הודעת שגיאה
# 4. [2,3,4]



# EX 8.2.1
data = ("self", "py", 1.543)
format_string = "Hello %s.%s learner, you have %.1f units left before you master the course!"
print(format_string % data)


# EX 8.2.2
def sort_prices(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: x[1], reverse=True)


# EX 8.2.3
def mult_tuple(tuple1, tuple2):
    pairs = ()
    for item1 in tuple1:
        for item2 in tuple2:
            pairs += (item1, item2), (item2, item1)
    return pairs


# EX 8.2.4
def sort_anagrams(list_of_strings):
    anagrams_dict = {}
    for main_word in list_of_strings:
        found = False
        for key in anagrams_dict:
            if set(main_word.lower()) == set(key.lower()):
                if main_word not in anagrams_dict[key]:
                    anagrams_dict[key].append(main_word)
                found = True
                break
        if not found:
            anagrams_dict[main_word] = [main_word]
            for word in list_of_strings:
                if word != main_word and set(word.lower()) == set(main_word.lower()):
                    anagrams_dict[main_word].append(word)
    return list(anagrams_dict.values())



# EX 8.3.1
# 1. (2 ,1) ואז (3 ,2)
# 2. 1 ואז 2
# 3. 2
# 4. הודעת שגיאה מסוג KeyError
# 5. 1


# EX 8.3.2
import datetime

person = {"first_name":"Mariah", "last_name":"Carey", "birth_date":"27.03.1970", "hobbies":["Sing", "Compose", "Act"]}
function = int(input("Enter function number 1-7"))
while True:
    if function == 1:
        print(person["last_name"])
    if function == 2:
        print(person["birth_date"].split(".")[1])
    elif function == 3:
        print(f"{person['first_name']} has {len(person['hobbies'])} hobbies")
    elif function == 4:
        print(person['hobbies'][-1])
    elif function == 5:
        person["hobbies"].append("Cooking")
    elif function == 6:
        person["birth_date"] = tuple(person["birth_date"].split("."))
    elif function == 7:
        if isinstance(person["birth_date"], str):
            day, month, year = map(int, person["birth_date"].split("."))

        else:
            day, month, year = person["birth_date"]
        today = datetime.date.today()
        age = today.year - int(year) - ((today.month, today.day) < (int(month), int(day)))
        person["age"] = age
        print(f"{person['first_name']}'s age is {age}")
    function = int(input("Enter function number 1-7"))


# EX 8.3.3
def count_chars(my_str):
    letter_count = {}
    for char in my_str:
        if char.isalpha():
            char = char.lower()
            letter_count[char] = letter_count.get(char, 0) + 1
    return letter_count


# EX 8.3.4
def inverse_dict(my_dict):
    reversed_dict = {}
    for key, value in my_dict.items():
        if value not in reversed_dict:
            reversed_dict[value] = [key]
        else:
            reversed_dict[value].append(key)
    for key in reversed_dict:
        reversed_dict[key].sort()
    return reversed_dict



# EX 8.4.1
def print_hangman(num_of_tries):
    HANGMAN_PHOTOS = {0:"    x-------x",1: """    x-------x
    |
    |
    |
    |
    |
""",2: """    x-------x
    |       |
    |       0
    |
    |
    |""", 3:"""    x-------x
    |       |
    |       0
    |       |
    |
    |""",4: """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""",5: """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""",6: """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""}
    print(HANGMAN_PHOTOS[num_of_tries])