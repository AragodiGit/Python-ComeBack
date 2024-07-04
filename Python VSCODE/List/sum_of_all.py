def sum_of_list_item(ls):
    sum = 0
    for item in ls:
        sum += item
    return sum

n = int(input("Enter number of items:"))
ls = []
for i in range(n):
    val = int(input("Enter the item:"))
    ls.append(val)

obj = sum_of_list_item(ls)
print(f"The sum of the list item:{obj}")
