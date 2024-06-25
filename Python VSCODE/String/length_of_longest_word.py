def find_long_lenght(word_list):
    ans_list = []
    for i in word_list:
        ans_list.append((len(i),i))

    ans_list.sort()

    # print(ans_list)

    # print(ans_list[-1])

    return ans_list[-1][1], ans_list[-1][0]

ans = find_long_lenght(["PHP", "Exercises", "Backend"]) 
print(f"Longest word: {ans[0]}")
print(f"lenght of word: {ans[1]}")

