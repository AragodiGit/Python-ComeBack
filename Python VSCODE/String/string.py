def change_char(s):
    char = s[0]
    str1 = s.replace(char, "$")
    str1 = char + str1[1:]

    return str1
obj = change_char("restart")
print(obj)