import sys
import os

sys.path.insert(0, os.environ['USERPROFILE'] + '\\Documents\\Personal_Code_Projects\\Python\\30-Days-Of-Python\\data')

from countries import countries 

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()

ages.append(ages[0])
ages.append(ages[-1])

ages.sort()

print('Sorted List of Students Ages:', ages)

median_age = (ages[5] + ages[6]) / 2

average_age = sum(ages) / len(ages)

min_age = ages[0]

max_age = ages[-1]

print('Median Age:', median_age)

print('Average Age of the Student in the List:', average_age)

print('Age Range of the Students on the List:', ages[-1] - ages[0], 'Years')

min_span = round(abs(min_age - average_age),2)

max_span = round(abs(max_age - average_age),2)

print('Min to Average Age Span:', min_span, ', Max to Average Age Span:', max_span)

print(round(len(countries) / 2) - 1)

print(len(countries) / 2)

print(countries[95])

Afghanistan, Albania, Algeria, *rest = countries

print(Afghanistan)
print(Albania)
print(Algeria)
#print(rest)