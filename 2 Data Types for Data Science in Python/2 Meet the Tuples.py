my_tuple = 'el_1', 'el_2', 'el_2'
second_tuple = 'a', 'b', 'c'
print(my_tuple, '\n')

# unpack tuple into multiple variables
el1, el2, el3 = my_tuple
print('values of el1, el2, el3: ->', el1, el2, el3, '\n')

# zip()
my_zip = zip(my_tuple, second_tuple)
print('my_zip: ->', my_zip)
print('list(my_zip): ->', list(my_zip), '\n')
# when you unpack/unzip the zip, the zip will be empty
print("when you unpack/unzip the zip, the zip will be empty:")
print('my_zip: ->', my_zip, "<- it's still the same object")
print('list(my_zip): ->', list(my_zip), "<- but here is empty because we unzip it above", '\n')


# enumerate()
print('for position, item in enumerate(my_zip): ->')
my_zip = zip(my_tuple, second_tuple)
for position, item in enumerate(my_zip):
    print(position, item)

print('for position, item in enumerate(my_zip): item1, item2 = item: ->')
my_zip1 = zip(my_tuple, second_tuple)
for position, item in enumerate(my_zip1):
    item1, item2 = item
    print(position, item1, item2)
