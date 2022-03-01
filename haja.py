
from random import randint
from string import ascii_uppercase 
import pandas as pd

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

# Print pandas dataframe
def print_full_table(data):
    table = pd.DataFrame(data, index=['Monday', 'Tuesday', 'Wednsday'])
    for i in range(len(table)):
        for b in range(len(table)):
            classs = table.iloc[i, b]
            table.iloc[i, b] = f"{classs.code} - {classs.name}"

    table.rename({'Monday':1,"Tuesday":2,"Wednesday":3}, axis = 1, inplace=True)
    print(table.to_string())

time_table = {
   "Monday": [],
   "Tuesday": [],
   "Wednesday": []
}

for day in time_table.keys():
    for period in range(3):
        classs = Subject(random_str(6), random_str(15))
        time_table[day].append(classs)




print_full_table(time_table)