def sum_of_list_item(ls):
    ls.sort()
    return ls[-1]

n = int(input("Enter number of items:"))
ls = []
for i in range(n):
    val = int(input("Enter the item:"))
    ls.append(val)

obj = sum_of_list_item(ls)
print(f"The largest number of list:{obj}")
