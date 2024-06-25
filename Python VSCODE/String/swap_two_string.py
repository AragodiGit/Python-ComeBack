def swap_two_string(s1,s2):
    first = s2[:2] + s1[2]
    second = s1[:2] + s2[2]
    return (first + ' ' + second)
obj = swap_two_string('abc', 'xyz')
print(obj)