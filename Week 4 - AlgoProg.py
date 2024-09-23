'''RAAAAAHHHH'''
# Michael Arianno Chandrarieta - 2802499711

# unify them thingymajigs
def unify_lists(A, B):
    return list(set(A).union(set(B)))

# modify them thingymajigs
def modify_string(tup, string):
    return ''.join([char * times for char, times in zip(string, tup)])

# pacient 0
a1, b1 = [1, 3, 5], [1, 2, 3]
a2, b2 = [2, 4, 6], [2, 4, 6]
a3, b3 = [1, 2, 3, 4], [4, 5, 6, 7]

# pacient 0 (2.0)
tup1, str1 = (1, 2, 3, 4), 'alex'
tup2, str2 = (1, 2, 1), 'pan'
tup3, str3 = (5,), 'z'

unify_results = [unify_lists(a1, b1), unify_lists(a2, b2), unify_lists(a3, b3)]
modify_results = [modify_string(tup1, str1), modify_string(tup2, str2), modify_string(tup3, str3)]

print(unify_results)
print(modify_results)