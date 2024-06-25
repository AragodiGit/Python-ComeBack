def natural_sum(listt):
    ans = []
    for i in listt:
        ans.append(i*i)
    return sum(ans)

n = int(input("Enter value for n:"))
in_list = []

for i in range(n):
    x = int(input("Enter value: "))
    in_list.append(x)

obj = natural_sum(in_list)
print("sum of square of n natural numbers is:", obj)
