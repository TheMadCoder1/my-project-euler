def prime_factorize(num):
    factors = []
    while num > 1:
        prime = 2
        while True:
            if num % prime == 0:
                factors.append(prime)
                num = num / prime
                break
            prime += 1
    return factors

print prime_factorize(600851475143)[-1]
