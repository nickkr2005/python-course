# UNIT 7


# EX 7.1.1
# מודפס wow ובשורה הבאה wow.


# EX 7.1.2
# מודפס 6.


# EX 7.1.3
# 1. מודפס 10, בשורה הבאה 9, אז 8, אז 7 ואז 6.
# 2. מודפס 10, בשורה הבאה 9, אז 8, אז 7, אז 6, אז 4, אז 3, אז 2, אז 1 ואז 0.


# EX 7.1.4
def squared_numbers(start, stop):
    lst = []
    while start <= stop:
        lst.append(start**2)
        start+=1
    return lst



# EX 7.2.1
def is_greater(my_list, n):
    lst = []
    for num in my_list:
        if num>n:
            lst.append(num)
    return lst


# EX 7.2.2
def numbers_letters_count(my_str):
    dig_count = 0
    let_count = 0
    for chr in my_str:
        if chr.isnumeric():
            dig_count +=1
        else:
            let_count +=1
    return [dig_count, let_count]


# EX 7.2.3
# C: (0, -10, -3)
# D: (0, -12, -3)


# EX 7.2.4
def seven_boom(end_number):
    lst = ["BOOM"]
    for i in range(1,end_number+1):
        if 7%i == 0 or '7' in str(i):
            lst.append("BOOM")
        else:
            lst.append(i)
    return lst


# EX 7.2.5
def sequence_del(my_str):
    new_str = my_str[0]
    for chr in my_str:
        if chr != new_str[-1]:
            new_str+=chr
    return new_str


# EX 7.2.6
def print_illegal(cart):
    for item in cart:
        if len(item)<3 or not item.isalpha():
            print(item)

def remove_duplicates(cart):
    new_cart = []
    for item in cart:
        if item not in new_cart:
            new_cart.append(item)
    return new_cart

def main():
    cart = input("Please enter shopping cart: ").split(",")
    function = int(input("Enter what function would you like to do: "))
    while function != 9:
        if function == 1:
            print(f"your shopping cart: {cart}")
        elif function == 2:
            print(f"There are {len(cart)} items in your cart")
        elif function == 3:
            print(f"Is item in cart? {input('Enter item to check: ') in cart}")
        elif function == 4:
            cart.remove(input("enter item to remove from your cart: "))
        elif function == 6:
            cart.append(input("Enter item to add to the cart: "))
        elif function == 7:
            print_illegal(cart)
        elif function == 8:
            cart = remove_duplicates(cart)
        function = int(input("Enter what function would you like to do: "))

if __name__ == "__main__":
    main()


# EX 7.2.7
def arrow(my_char, max_length):
    i,d=1,1
    while i!=0:
        if i==max_length:
            d=-1
        print(my_char*i)
        i+=d



# EX 7.3.1
def show_hidden_word(secret_word, old_letters_guessed):
    progress = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            progress += letter + " "
        else:
            progress += "_ "
    return progress


# EX 7.3.2
def check_win(secret_word, old_letters_guessed):
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True