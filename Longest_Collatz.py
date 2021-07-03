MAX = 1000000-1
cache = {}
cache[0] = 0
cache[1] = 1

def collatz_len(num):
    stack = [num]
    while stack:
        num = stack.pop()
        next_num = num//2 if num%2==0 else 3*num + 1
        if num in cache:
            continue
        if next_num in cache:
            cache[num] = cache[next_num] + 1
        else:
            stack.append(num)
            stack.append(next_num)
    return cache[num]


max_num = 1
for i in range(2, MAX+1):
    max_num = max(max_num, i, key=collatz_len)

print("Longest length: {}".format(cache[max_num]))
print("Starting number: {}".format(max_num))