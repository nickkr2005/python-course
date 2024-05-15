# UNIT 5


# EX 5.1.1
# המשתנה item מצביע בכל איטרציה על ערכו של האיבר הבא ברשימה
# הלולאה for קוראת מאחורי הקלעים לפונקציה next וערך ההחזרה שלה מושם למשתנה item


# EX 5.1.2
import winsound

freqs = {"la": 220, "si": 247, "do": 261, "re": 293, "mi": 329, "fa": 349, "sol": 392,}
notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"
iter_notes = iter(notes.split("-"))
for note in iter_notes:
    splitted = note.split(",")
    winsound.Beep(freqs[splitted[0]], int(splitted[1]))



# EX 5.2.1
# אובייקט המוחזר מהפונקציה iter
# אובייקט המוחזר מהפונקציה filter


# EX 5.2.2
numbers = iter(list(range(1, 101,3)))
for i in numbers:
    print(i)


# EX 5.2.3
from itertools import combinations

def find_combinations():
    bills = [20] * 3 + [10] * 5 + [5] * 2 + [1] * 5
    count = 0
    for i in range(1,len(bills)+1):
        unique_permutations = set(combinations(bills,i))
        for perm in unique_permutations:
                if sum(perm) == 100:
                    print(perm)
                    count += 1
    return count

def main():
    print(find_combinations())

if __name__ == "__main__":
    main()



# EX 5.3.1
# כל גנרטור הוא איטרטור
# כל איטרטור הוא איטרבל


# EX 5.3.2
class MusicNotes():
    def __init__(self):
        self._notes = {"La":55,"Si":61.74,"Do":65.41,"Re":73.42,"Mi":82.41,"Fa":87.31,"Sol":98}
        self._octava = 0
        self._note = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self._note == 6:
            self._note = -1
            if self._octava == 0 or 1:
                self._octava += 1
            else:
                self._octava **= 2
        if self._octava >= 5:
            raise StopIteration()
        self._note += 1
        return list(self._notes.values())[self._note] * (2 ** self._octava)

def main():
    notes_iter = iter(MusicNotes())
    for freq in notes_iter:
        print(freq)

if __name__ == "__main__":
    main()



# EX 5.4

def check_id_valid(id_number):
    """Checks if ID number is valid.
    :param id_number: the ID number to check.
    :type id_number: int.
    :return: Is the passed ID number valid
    :rtype: bool
    """
    return sum(int(digit) if i % 2 == 0 else sum(map(int, str(int(digit) * 2))) for i, digit in enumerate(str(id_number))) % 10 == 0

class IDIterator():
    """
    This class is used to represent the ID iterator
    """

    def __init__(self,id=0):
        """Creates a new ID iterator object and sets the variables of the class
        :param id: Starting ID number.
        :type id_number: int.
        :return: None
        """
        self._id = id

    def __iter__(self):
        """:Returns the iterator object
        :return: Iterator object.
        :rtype: IDIterator object
        """
        return self

    def __next__(self):
        """:Returns the next valid ID number.
        :return: ID number.
        :rtype: int
        :raise: StopIteration: raises an Exception when the last ID number in the valid range has been reached.
        """
        self._id += 1
        if self._id >= 1000000000:
            raise StopIteration()
        while not check_id_valid(self._id):
            self._id += 1
        return self._id

def id_generator(ID):
    """Creates a ID generator.
    :param ID: the ID number to check.
    :type ID: int.
    :return: Valid ID number generator.
    :rtype: Generator
    """
    ID += 1
    while ID < 1000000000:
        if check_id_valid(ID):
            yield ID
        ID += 1

def main():
    """This is the main function of the program.
    """
    id = int(input("enter ID: "))
    option = input("Generator or Iterator? (gen/it)? ")
    if option == "gen":
        IDgen = id_generator(id)
        for i in range(10):
            print(next(IDgen))

    elif option == "it":
        IDiter = iter(IDIterator(id))
        for i in range(10):
            print(IDiter.__next__())

if __name__ == "__main__":
    main()