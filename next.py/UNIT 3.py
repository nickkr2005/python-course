# UNIT 3


# EX 3.1.1
# 1. IndexError
# 2. NameError
# 3. TypeError
# 4. ValueError


# EX 3.1.2
# חריגה מסוג AssignmentError.


# EX 3.1.3
def ThrowStopIteration():
    raise StopIteration()

def ThrowZeroDivisionError():
    raise ZeroDivisionError()

def ThrowAssertionError():
    raise AssertionError()

def ThrowImportError():
    raise ImportError()

def ThrowKeyError():
    raise KeyError()

def ThrowSyntaxError():
    raise SyntaxError()

def ThrowIndentationError():
    raise IndentationError()

def ThrowTypeError():
    raise TypeError()



# EX 3.2.1
# 0 או יותר


# EX 3.2.2
# כאשר לא נזרקת חריגה


# EX 3.2.3
# finally


# EX 3.2.4
# ArithmeticError


# EX 3.2.5
def read_file(file_name):
    try:
        data = open(file_name,"r").read()
    except:
        data = "__NO_SUCH_FILE__"
    finally:
        return f"__CONTENT_START__\n{data}\n__CONTENT_END__"



# EX 3.3.1
# התוכנית תקרוס בגלל קוד לא תקין.


# EX 3.3.2
class UnderAgeError(Exception):
    def __init__(self, age):
        self._age = age

    def __str__(self):
        return "You are only %d years old! come back in %d years, when you are 18." % (self._age, int(18 - self._age))

def send_invitation(name, age):
    if int(age) < 18:
        raise UnderAgeError(age)
    else:
        print("You should send an invite to " + name)



# EX 3.4
import string, re

class UsernameContainsIllegalCharacterError(Exception):
    def __init__(self,username):
        self._username = username
        self._index = re.search('[^a-zA-Z0-9_]', username).start()

    def __str__(self):
        return 'The username contains an Illegal character "%c" at index %d'%(self._username[self._index],self._index)

class UsernameTooShortError(Exception):
    def __str__(self):
        return "The username is too short"

class UsernameTooLongError(Exception):
    def __str__(self):
        return "The username is too long"

class PasswordMissingCharacterError(Exception):
    def __init__(self,password):
        self._password = password

    def __str__(self):
        return "The password is missing a character" + self.create_specific_error()

    def create_specific_error(self):
        if not any(char.isupper() for char in self._password):
            return UppercaseMissingError.__str__(self._password)
        elif not any(char.islower() for char in self._password):
            return LowercaseMissingError.__str__(self._password)
        elif not any(char.isdigit() for char in self._password):
            return DigitMissingError.__str__(self._password)
        elif not any(char in string.punctuation for char in self._password):
            return SpecialMissingError.__str__(self._password)

class PasswordTooShortError(Exception):
    def __str__(self):
        return "The password is too short"

class PasswordTooLongError(Exception):
    def __str__(self):
        return "The username is too long"

class UppercaseMissingError(PasswordMissingCharacterError):
    def __str__(self):
        return " (Uppercase)"

class LowercaseMissingError(PasswordMissingCharacterError):
    def __str__(self):
        return " (Lowercase)"

class DigitMissingError(PasswordMissingCharacterError):
    def __str__(self):
        return " (Digit)"

class SpecialMissingError(PasswordMissingCharacterError):
    def __str__(self):
        return  " (Special)"

def check_input(username, password):
    if len(username)<3:
        raise UsernameTooShortError()
    if len(username)>16:
        raise UsernameTooLongError()
    if not bool(re.match('^[a-zA-Z0-9_]+$', username)):
        raise UsernameContainsIllegalCharacterError(username)
    if len(password)<8:
        raise PasswordTooShortError()
    if len(password)>40:
        raise PasswordTooLongError()
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    if not has_uppercase or not has_lowercase or not has_digit or not has_special:
        raise PasswordMissingCharacterError(password)
    print("OK")

def main():
    while True:
        username = input("enter your username")
        password = input("enter your password")
        try:
            check_input(username,password)
        except UsernameContainsIllegalCharacterError as e:
            print(e)
        except UsernameTooLongError as e:
            print(e)
        except UsernameTooShortError as e:
            print(e)
        except PasswordTooShortError as e:
            print(e)
        except PasswordTooLongError as e:
            print(e)
        except PasswordMissingCharacterError as e:
            print(e)
        else:
            break

if __name__ == "__main__":
    main()