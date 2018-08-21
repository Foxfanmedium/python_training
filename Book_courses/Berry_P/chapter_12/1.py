# import os
#
# with open('buzzers.csv', 'r') as raw_data:
#     print(raw_data.read())
#====================================================================================================================
# import csv
#
# with open('buzzers.csv') as data:
#     for line in csv.reader(data):
#         print(line)
#====================================================================================================================
# import csv
#
# with open ('buzzers.csv') as data:
#     for line in csv.DictReader(data):
#         print(line)
#====================================================================================================================
from datetime import datetime
import csv
import pprint


def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%Mp')


with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k,v = line.strip().split(',')
        flights[k] = v

# pprint.pprint(flights)
# print()
#
# flights2 = {}
# for k, v in flights.items():
#     flights2[convert2ampm(k)] = v.title()
# pprint.pprint(flights2)

# more_dest = [dest.title() for dest in flights.values()]
# print(more_dest)
#
# ft = [convert2ampm(ft) for ft in flights.keys()]
# print(ft)
#
#
# more_flights = {convert2ampm(k): v.title() for k,v in flights.items()}
# print(more_flights)

just_freeport = {}
for k,v in flights.items():
    if v == 'FREEPORT':
        just_freeport[convert2ampm(k)] = v.title()
    print(just_freeport)

just_freeport2 = {convert2ampm(k): v.title() for k,v in flights.items() if v == 'FREEPORT'}
print(just_freeport2)

fts = {convert2ampm(k):v.title() for k,v in flights.items()}
print(fts)

dest = set(fts.values())
# print(dest)
#
# wests = []
# for k,v in fts.items():
#     if v == 'West End':
#         wests.append(k)

west2 = [k for k,v in fts.items() if v =='West End']

when = {}
for dest in set(fts.values()):
    when[dest] = [k for k in fts.items() if v == dest]

pprint.pprint(when)


when2 = {dest: [k for k, v in fts.items() if v==dest] for dest in set(fts.values())}

