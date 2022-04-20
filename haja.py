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


def generate_empty_time_table(period_num):
    days = ("Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday")
    periods = ["" for i in range(period_num)]
    return {day:periods.copy() for day in days}


if __name__ == "__main__":

    subjects = {}
    data = pd.read_excel('dataset.xlsx',sheet_name = 'Sheet2')
    data.set_index('days', inplace=True)

    days_index = list(data.index)
    number_of_periods = len(data.columns)

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

    separated_subjects = {}
    for i in subjects.keys():
        subject = subjects[i]

        if subject.code not in separated_subjects.keys():
            separated_subjects[subject.code] = [subject]

        else:
            separated_subjects[subject.code].append(subject)

    separated_subjects_arr = [separated_subjects[key] for key in separated_subjects.keys()]
    valid_possibilities = []
    valid_time_tables = []
    valid = True

    # Find all the possibilities using cartesian product method
    for possibility in itertools.product(*separated_subjects_arr):
        valid = True
        time_table = generate_empty_time_table(number_of_periods)

        for subject in possibility:

            for time_slot in subject.time_slots:

                if time_table[time_slot.day][time_slot.period] == "":
                    time_table[time_slot.day][time_slot.period] = f'{subject.code}({subject.group})'
                else:
                    valid = False
                    continue

            if not valid: continue

        if valid:
            valid_possibilities.append(possibility)
            valid_time_tables.append(time_table)
