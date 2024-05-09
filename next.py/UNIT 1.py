# UNIT 1


# EX 1.1.1
# 3. 12


# EX 1.1.2
def double_letter(my_str):
    return "".join(list(map(lambda a: 2*a, my_str)))


# EX 1.1.3
def four_dividers(number):
    return list(filter(lambda x:x%4==0, range(1,number+1)))


# EX 1.1.4
def sum_of_digits(number):
    return functools.reduce(lambda x, y: x + y, map(int, str(number)))



# EX 1.2.1
# 1


# EX 1.2.2
# x


# EX 1.2.3
# x+y


# EX 1.2.4
# y


# EX 1.2.5
# 4. 1234



# EX 1.3.1
def intersection(list_1, list_2):
    return list(set(list_1) & set(list_2))


# EX 1.3.2
def is_prime(number):
    return len([x for x in range(1,number+1) if number%x==0]) == 2


# EX 1.3.3
def is_funny(string):
    return len([ch for ch in string if ch!='h' and ch!='a']) == 0


# EX 1.3.4
dec_password = (lambda s: ''.join(chr(((ord(char) - 97 + 2) % 26) + 97) if char.islower() else chr(((ord(char) - 65 + 2) % 26) + 65) if char.isupper() else char for char in s))(password)



# EX 1.5
import functools

file_path = "C:\\Users\\NickKR\\OneDrive\Documents\\names.txt"
with open(file_path,"r") as file:
    names = file.read().split("\n")
    print(f"1. longest name: {max(map(str, names), key=len)}")
    print(f"2. total names length: {functools.reduce(lambda x,y:x+y,(map(len, names)))}")
    shortest_names = '\n'.join([name for name in names if len(name) == min(map(len, names))])
    print(f"3. shortest names: {shortest_names}")
    print(f"4. names length: ")
    [print(len(name)) for name in names]
    length = int(input('enter length: '))
    matching_names = '\n'.join([name for name in names if len(name) == length])
    print(f"5. names matching length: {matching_names}")
