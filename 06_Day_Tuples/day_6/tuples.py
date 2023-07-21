

empty_tuple = ()

sisters = ('li', 'el', 'sha')

brothers = ('lo', 'tay', 'jo')

siblings = sisters + brothers

print(len(siblings))

parents = ('Joh', 'Eliza')

family_members = siblings + parents

print(family_members)

unpacked_siblings = family_members[0:6]

unpacked_parents = family_members[6:]

fruits = ('mango', 'lime', 'lemon')

vegetables = ('onion', 'celery', 'carrot')

animal_prod = ('milk', 'cheese', 'broth')

food_stuff_tp = fruits + vegetables + animal_prod

food_stuff_list = list(food_stuff_tp)

print(food_stuff_list)

food_stuff_list.remove(food_stuff_tp[int(len(food_stuff_tp) / 2)])

print(food_stuff_list)

print(food_stuff_list[3:5])

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Is Estonia in the Nordic Countries:', 'Estonia' in nordic_countries)

print('Is Iceland in the Nordic Countries:', 'Iceland' in nordic_countries)