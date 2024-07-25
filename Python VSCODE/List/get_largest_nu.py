def sum_of_list_item(ls):
    count = 0
    for item in ls:
        if len(item) > 2:
            if item[0] == item[-1]:
                count += 1
    return count
        

ls = ['abc', 'xyz', 'aba', '1221','aja']
obj = sum_of_list_item(ls)
print(obj)
