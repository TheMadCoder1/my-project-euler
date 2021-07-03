lst = []
with open("tri.txt", "r") as f:
    for line in f:
        lst.append([int(x) for x in line.split(" ")])

dim = len(lst)

totals = [[0]*(dim+1) for _ in range(dim+1)]

""" Top of triangle to bottom """
# for level in range(dim):
#     for i in range(1, (level+1)+1):
#         totals[level+1][i] = lst[level][i-1] + max(totals[level][i-1], totals[level][i])
#     print(" ".join(map(str, totals[level+1])))
#     print(lst[level])

# max_num = 0
# for num in totals[-1]:
#     max_num = max(max_num, num)
# print(max_num)

""" Base to top """
for level in range(dim-1, -1, -1):
    for i in range(level+1):
        totals[level][i] = lst[level][i] + max(totals[level+1][i], totals[level+1][i+1])
    # print(" ".join(map(str, totals[level+1])))
    # print(lst[level])

print(totals[0][0])