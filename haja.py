
from random import randint
from string import ascii_uppercase 

global characters
characters = ascii_uppercase + "0123456789"

def random_str(length):
    rstr = ""
    for i in range(length):
        index = randint(0, len(characters)-1)
        char = characters[index]
        rstr += char
    return rstr

class Subject:
    
    def __init__(self, code, name):
        self.code = code
        self.name = name

time_table = {
   "Monday": [],
   "Tuesday": [],
   "Wednesday": []
}

for day in time_table.keys():
    for period in range(3):
        classs = Subject(random_str(6), random_str(15))
        time_table[day].append(classs)


print(time_table)
