# for later use: my_list = ['el_1', 'el_2', 'el_3']

# items in the list may repeat
my_list = ['el_1', 'el_2', 'el_2']
print(my_list, '\n')

my_list = ['el_1', 'el_2', 'el_3']
print(my_list, '\n')

'''methods'''
# .append(item) <- add new item at the end of the list
my_list.append('el_4')
print('.append("el_4"):', my_list, '\n')

# .extend(array) <- combine list with array (add array items to list) (the items could double inside the list)
# my_list.extend(my_list) === my_list + my_list
my_list.extend(my_list)
print('.extend(array):', my_list, '\n')

# .index(item) -> return index of item
position = my_list.index('el_2')
print('.index("el_2"): ->', position, '\n')

# .pop(item_index) -> pop out item from list (also save it into "cache" to use this item later)
pop = my_list.pop(position)
print(".pop('el_2'):", pop, '\n')

# sorted(list) -> create new list with sorted elements (sorted eith ascending values) from previous list
sorted_list = sorted(my_list)
print('sorted(my_list): ->', sorted_list)
print('id(sorted_list):', id(sorted_list), 'id(my_list): ', id(my_list))
print('are ids of sorted_list and my_list equal?: ', sorted_list == my_list, '\n')
