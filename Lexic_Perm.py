facts = [1] * 10
for i in range(1, 10):
    facts[i] = facts[i-1]*i

def get_perm(target, max_digit):
    arr = []
    remaining = list(range(max_digit+1))

    perm_left = target-1
    for i in range(max_digit, -1, -1):
        ind = perm_left // facts[i]
        perm_left %= facts[i]
        arr.append(remaining[ind])
        del remaining[ind]
    return "".join(map(str, arr))

print(get_perm(10**6, 9))