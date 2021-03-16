# Sets are created from a list
list_1 = ['a', 'b', 'c', 'd', 'e']
list_2 = ['d', 'e', 'f', 'g', 'h']
# creating sets
set_1 = set(list_1)
set_2 = set(list_2)
# compare list and sets
print("list_1: -> ", list_1)
print('set_1: -> ', set_1)
print("list_2: -> ", list_2)
print('set_2: -> ', set_2, '\n')

# .union() (or)
print('# .union() (or)')
union_set_1 = set_1.union(set_2)
union_set_2 = set_2.union(set_1)
print('union_set_1: ->', union_set_1)
print('union_set_2: ->', union_set_2)
print("union_set_1 == union_set_2 ?: ->", union_set_1 == union_set_2, '\n')

# .intersection() (and)
print('# .intersection() (and)')
intersection_set_1 = set_1.intersection(set_2)
intersection_set_2 = set_2.intersection(set_1)
print('intersection_set_1: ->', intersection_set_1)
print('intersection_set_2: ->', intersection_set_2)
print("intersection_set_1 == intersection_set_2 ?: ->", intersection_set_1 == intersection_set_2, '\n')

# .difference() (-)
print('# .difference() (-)')
difference_set_1 = set_1.difference(set_2)
difference_set_2 = set_2.difference(set_1)
print('difference_set_1: ->', difference_set_1)
print('difference_set_2: ->', difference_set_2)
print("difference_set_1 == difference_set_2 ?: ->", difference_set_1 == difference_set_2, '\n')

# .add(item)
print('# .add(item)')
print('print(set_1): ->', set_1)
set_1.add('z')
print("'z' added: ->", set_1)
set_1.add('a')
print("'a' added: ->", set_1, '\n',
      "<- nothing happend because 'a' was already there (and sets doesn't keep same values", '\n')

# .update(item/array)
print('# .update(item/array)')
set_1.update('w')
print("'w' added: ->", set_1)
set_1.update(['y', 'x'])
print("'x' and 'y' added: ->", set_1)
set_1.update('a', 'b')
print("'a' and 'b' added: ->", set_1,
      "<- nothing happend because 'a' was already there (and sets doesn't keep same values", '\n')

# .discard()
print('# .discard()')
print('print(set_2): ->', set_2)
set_2.discard('h')
print("'h' discarded: ->", set_2, '\n')

# .pop() take no arguments
print('# .pop()')
print('print(set_2): ->', set_2)
print('pop: ->', set_2.pop())
print("poped set_2: ->", set_2, '\n')
