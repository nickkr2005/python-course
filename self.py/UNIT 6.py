# UNIT 6


# EX 6.1.1
# 1. first_list[2][1] % first_list[1][1] = 5
# 2. second_list[1][0][1] = 6


# EX 6.1.2
def shift_left(my_list):
    return [my_list[1],my_list[2],my_list[0]]



# EX 6.2.1
# 1. 7
# 2. 1
# 3. 8
# 4. תתקבל הודעת שגיאה
# 5. 4
# 6. 6


# EX 6.2.2
# A: programming_languages[2][0]
# B: programming_languages[3][0]
# D: programming_languages[-2][0]
# E: programming_languages[-1][-4]
# F: programming_languages[-4][-1]
# G: programming_languages[2]
# I: programming_languages[-2]


# EX 6.2.3
def format_list(lst):
    return ", ".join(lst[::2]) + f" and {lst[-1]}"


# EX 6.2.4
def extend_list_x(list_x, list_y):
    list_x[:0] = list_y
    return list_x



# EX 6.3.1
def are_lists_equal(list1, list2):
    return sorted(list1) == sorted(list2)


# EX 6.3.2
def longest(my_list):
    return sorted(my_list,key=len,reverse=True)[0]



# EX 6.4.1
def check_valid_input(letter_guessed, old_letters_guessed):
    if len(letter_guessed) > 1 or not letter_guessed.isalpha():
        return False
    return letter_guessed.lower() not in old_letters_guessed


# EX 6.4.2
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed,old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    print(f"X\n{' -> '.join(old_letters_guessed)}")
    return False
