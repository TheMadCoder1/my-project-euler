MAX = 2000000
is_prime = [True] * (MAX+1)
total = 0
for i in range(2, MAX+1):
    if is_prime[i]:
        total += i
        for i in range(i+i, MAX+1, i):
            is_prime[i] = False
print(total)