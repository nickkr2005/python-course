# UNIT 3

# EX 3.1.1
# 'Hello Python 3.6.3'



# EX 3.2.1
print("\"Shuffle, Shuffle, Shuffle\", say it together!\nChange colors and directions,\nDon't back down and stop the player!\n\tDo you want to play Taki?\n\tPress y\\n")



# EX 3.3.1
# numbers[0:10:1] = '123456789'
# numbers[3:6:3] = '4'
# numbers[-1:-10] = ''


# EX 3.3.2
# syzygy


# EX 3.3.3
encrypted_message = "!XgXnXiXcXiXlXsX XnXoXhXtXyXpX XgXnXiXnXrXaXeXlX XmXaX XI"
dec = encrypted_message[::-2]
print(dec) # I am learning python slicing!



# EX 3.4.1
# spaceship


# EX 3.4.2
str = input("Please enter a string: ")
str = str [0] + str[1:].replace(str[0],'e')
print(str) 


# EX 3.4.3
import math
str = input("Please enter a string: ")
middle = math.floor(len(str)/2)
str = str[:middle] + str[middle:].upper()
print(str)


# EX 3.4.4
LAUNCH_DATE = "16/07/1969"
RETURN_DATE = "24/07/1969"
astronaut = "Neil" + "Armstrong"
days = how_many_days(LAUNCH_DATE‚ RETURN_DATE)
astronaut.take_to_space(days)



# EX 3.5.1
ch = input("Guess a letter:").lower()
print(ch)


# EX 3.5.2
str = input("Please enter a word: ")
form = "_ "*len(str)
print(form)