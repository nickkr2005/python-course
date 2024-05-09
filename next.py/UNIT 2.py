# UNIT 2


# EX 2.1.1
# מחלקה(class)


# EX 2.1.2
# 1. מופע של המחלקה
# 2. ערך של תכונה
# 3. מתודה
# 4. תכונה



# EX 2.2.1
# מתודת אתחול (init method)


# EX 2.2.2.
class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def birthday (self):
        self.age+=1

    def get_age(self):
        return self.age


def main():
    dog1 = dog("miles",9)
    dog2 = dog("koko",11)
    dog1.birthday()
    print(f"dog1 age: {dog1.get_age()}, dog2 age: {dog2.get_age()}")

if __name__ == "__main__":
    main()



# EX 2.3.1
# יודפס 123.


# EX 2.3.2
# יודפס למסך הכיתוב "hello world".


# EX 2.3.3
class dog:
    count_animals = 1

    def __init__(self,age,name="Octavio"):
        self._name = name
        self._age = age
        self.count_animals+=1

    def birthday (self):
        self._age+=1

    def get_age(self):
        return self._age

    def set_name(self, name):
        self._name=name

    def get_name(self):
        return self._name


def main():
    dog1 = dog(11,"miles")
    dog2 = dog(9)
    dog1.birthday()
    print(f"dog1 age: {dog1.get_name()}, dog2 age: {dog2.get_name()}")
    dog2.set_name("koko")
    print(f"new name for dog2: {dog2.get_name()}")
    print(f"count animals = {dog2.count_animals}")

if __name__ == "__main__":
    main()


# EX 2.3.4
class Pixel:

    def __init__(self,x=0,y=0,red=0,green=0,blue=0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        avg = int((self._blue + self._red + self._green)/3)
        self._blue = avg
        self._green = avg
        self._red = avg

    def print_pixel_info(self):
        amounts = [self._red, self._green, self._blue]
        colors = {"Red":amounts[0], "Green":amounts[1], "Blue":amounts[2]}
        zeros = [color for color in colors.keys() if colors[color]!=0]
        if len(zeros) == 1:
            print(f"X: {self._x,}, Y: {self._y}, Color: ({self._red},{self._green},{self._blue}) {zeros[0]}")
        else:
            print(f"X: {self._x,}, Y: {self._y}, Color: ({self._red},{self._green},{self._blue})")


def main():
    p = Pixel(5, 6, 250)
    p.print_pixel_info()
    p.set_grayscale()
    p.print_pixel_info()

if __name__ == "__main__":
    main()



# EX 2.4.1
# יודפס B.


# EX 2.4.2
class BigThing():
    def __init__(self, var):
        self.var = var

    def size(self):
        if isinstance(self.var,int):
            return self.var
        elif isinstance(self.var,list) or isinstance(self.var,dict) or isinstance(self.var,str):
            return len(self.var)

class BigCat(BigThing):
    def __init__(self,var,weight):
        BigThing.__init__(self,var)
        self.wight = weight

    def size(self):
        if self.wight>20:
            return "Very Fat"
        if self.wight>15:
            return "Fat"
        return "Ok"



# EX 2.5
class Animal():
    """This class represents the general Animal
        :param name: the name of the animal
        :param hunger: the hunger level of the animal
        :param zoo_name: the name of the zoo
        :type name: string
        :type hunger: int
        :type zoo_name: string
    """
    zoo_name = "Hayaton"

    def __init__(self,name,hunger=0):
        """Initialize the variables of the class
        :param name: the name of the animal
        :param hunger: the hunger level of the animal
        :type name: string
        :type hunger: int
        :return: None
        """
        self._name = name
        self._hunger = hunger

    def get_name(self):
        """This function returns the name of the animal
        :return: the name of the animal
        :rtype: string
        """
        return self._name

    def is_hungry(self):
        """This function checks if the animal is hungry
        :return: is the animal hungry?
        :rtype: bool
        """
        return self._hunger>0

    def feed(self):
        """This feed the animal by reducing its hunger level by 1
        :return: None
        """
        self._hunger-=1

    def talk(self):
        """This function makes the animals talk
        :return: None
        """
        pass

    def special_function(self):
        """This function activates the special abilities of all the animals
        :return: None
        """
        if isinstance(self,Dog):
            self.fetch_stick()
        elif isinstance(self,Cat):
            self.chase_laser()
        elif isinstance(self,Skunk):
            self.stink()
        elif isinstance(self,Unicorn):
            self.sing()
        elif isinstance(self,Dragon):
            self.breath_fire()


class Dog(Animal):
    """This class represents the Dog"""
    type = "Dog"

    def talk(self):
        """This function makes the dog talk
        :return: None
        """
        print("woof woof")

    def fetch_stick(self):
        """This function is the special ability of the dog
        :return: None
        """
        print("There you go, sir!")


class Cat(Animal):
    """This class represents the Cat
    :return: None
    """
    type = "Cat"

    def talk(self):
        """This function makes the cat talk
        :return: None
        """
        print("meow")

    def chase_laser(self):
        """This function is the special ability of the cat
        :return: None
        """
        print("Meeeeow")


class Skunk(Animal):
    """This class represents the skunk
        :param _stink_count: the stink count of the skunk
        :type _stink_count: int
    """
    type = "Skunk"

    def __init__(self, name,hunger,_stink_count=6):
        """Initialize the variables of the class
        :param name: the name of the animal
        :param hunger: the hunger level of the animal
        :param _stink_count: the stink count of the skunk
        :type name: string
        :type hunger: int
        :type _stink_count: int
        :return: None
        """
        Animal.__init__(self,name,hunger)
        self._stink_count=_stink_count

    def talk(self):
        """This function makes the skunk talk
        :return: None
        """
        print("tsssss")

    def stink(self):
        """This function is the special ability of the skunk
        :return: None
        """
        print("Dear lord!")


class Unicorn(Animal):
    """This class represents the Unicorn"""
    type = "Unicorn"

    def talk(self):
        """This function makes the unicorn talk
        :return: None
        """
        print("Good day, darling")

    def sing(self):
        """This function is the special ability of the unicorn
        :return: None
        """
        print("I’m not your toy...")


class Dragon(Animal):
    """This class represents the Dragon
        :param _color: the color of the dragon
        :type _color: string
    """
    type = "Dragon"

    def __init__(self, name,hunger,_color="Green"):
        """Initialize the variables of the class
        :param name: the name of the animal
        :param hunger: the hunger level of the animal
        :param _color: the color of the dragon
        :type name: string
        :type hunger: int
        :type _color: string
        :return: None
        """
        Animal.__init__(self,name,hunger)
        self._color=_color

    def talk(self):
        """This function makes the dragon talk
        :return: None
        """
        print("Raaaawr")

    def breath_fire(self):
        """This function is the special ability of the dragon
        :return: None
        """
        print("$@#$#@$")


def main():
    """This is the main function of the program"""

    dog = Dog("Brownie",10)
    cat = Cat("Zelda",2)
    skunk = Skunk("Stinky",0)
    unicorn = Unicorn("Keith",7)
    dragon = Dragon("Lizzy",1450)
    dog2 = Dog("Doggo",80)
    cat2 = Cat("Kitty",80)
    skunk2 = Skunk("Stinky Jr.",80)
    unicorn2 = Unicorn("Clair",80)
    dragon2 = Dragon("McFly",80)
    zoo_lst = [dog,cat,skunk,unicorn,dragon,dog2,cat2,skunk2,unicorn2,dragon2]
    for animal in zoo_lst:
        if animal.is_hungry():
            print(animal.type, animal.get_name())
            while animal.is_hungry():
                animal.feed()
        animal.talk()
        animal.special_function()
    print("zoo name - ", Animal.zoo_name)

if __name__ == "__main__":
    main()
