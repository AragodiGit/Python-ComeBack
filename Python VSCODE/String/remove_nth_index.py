def remove_nth_index(s,index):
    part1 = s[:index]
    part2 = s[index + 1:]

    return part1 + part2
index = int(input("Enter the index to remove:"))
obj = remove_nth_index("python", index)
print(obj)