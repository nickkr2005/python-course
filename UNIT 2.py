UNIT 2

// EX 2.1.1
1. 7 - int
2. "37"	- str
3. 37.00 - float
4. '34.56' - str
5. 56.789 - float
6. "tfs56" - str
7. 3.7 - float


// EX 2.1.2
4 10


// EX 2.2.1
1. true_or_false = "ron" != "ron" -> False
2. true_or_false = "a" in "alpha" -> True
3. true_or_false = "A" in "alpha" -> False
4. true_or_false = "alpha" < "beta" -> True
5. true_or_false = 1 < 2 < 1 -> False
6. true_or_false = 18 <= 22 < 30 -> True
7. true_or_false = not(10) -> False
8. true_or_false = (7 > 10) and (1 > 1)	-> False
9. true_or_false = (20 % 10 == 2) or (1 == 1) -> True



// EX 2.3.1
int(swan_height) = 90
int(fairy_tale) = ERROR
str(bool(eggs_num)) = 'True'


// EX 2.3.2
print(a == b) -> True
print(a != b) -> False


// EX 2.3.3
num = input("Enter three digits (each digit for one pig):")
total = sum(int(char) for char in num)
print(total)
print(int(total/len(num)))
print(total%len(num))
print(total%len(num) == 0)


// EX 2.4.1
מספר חשבון - ACCOUNT_NUMBER
סכום הכסם - amount_of_money


// EX 2.5.1
HANGMAN_ASCII_ART = """Welcome to the game Hangman
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/"""
MAX_TRIES = 6

print(f"{HANGMAN_ASCII_ART}\n{MAX_TRIES}")

