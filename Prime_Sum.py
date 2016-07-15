primes = [2]
result = 2
i = 3
while i <= 2000000:
    prime = True
    for num in primes:
        if i % num == 0:
            prime = False
            break
        if num * 2 > i:
            break
    if prime:
        primes.append(i)
        result += i
    i += 1
print result