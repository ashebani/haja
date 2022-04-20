from random import randint
from string import ascii_uppercase 
import pandas as pd
import itertools

global characters
characters = ascii_uppercase + "0123456789"

def random_str(length):
    rstr = ""
    for i in range(length):
        index = randint(0, len(characters)-1)
        char = characters[index]
        rstr += char
    return rstr


class TimeSlot:

    def __init__(self, day, period):
        self.day = day
        self.period = period


class Subject:
    
    def __init__(self, code, name, group, time_slots):
        self.code = code
        self.name = name
        self.group = group
        self.time_slots = time_slots



# Print pandas dataframe
def print_full_table(data):

    table = pd.DataFrame(data, index=['Monday', 'Tuesday', 'Wednsday'])
    for i in range(len(table)):
        for b in range(len(table)):
            class_ = table.iloc[i, b]
            table.iloc[i, b] = f"{class_.code} - {class_.name}"

    table.rename({'Monday':1,"Tuesday":2,"Wednesday":3}, axis = 1, inplace=True)
    print(table.to_string())


if __name__ == "__main__":

    time_table = {
       "Monday": [],
       "Tuesday": [],
       "Wednesday": []
    }


    subjects = {}
    data = pd.read_excel('dataset.xlsx',sheet_name = 'Sheet2')
    data.set_index('days', inplace=True)

    days_index = list(data.index)

    for i in range(len(data)):
        for j in range(len(data.columns)):
            cell = data.iloc[i, j]
            time_slot = TimeSlot(days_index[i], j)

            if type(cell) is not str: continue

            if cell not in subjects.keys():
                code = cell[0:7]
                group = cell[8]

                subjects[cell] = Subject(code, "", group, [time_slot])

            else:
                subjects[cell].time_slots.append(time_slot)

                [[],[],[],[]]

