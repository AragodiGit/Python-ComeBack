def adding_ing(string):
    if len(string) >= 3:
        if string.endswith('ing'):
            string = string + 'ly'
        else:
            string = string + 'ing'
        return string
    else:
        return ('Length of string is less than 3.')

obj = adding_ing('string')
print(obj)