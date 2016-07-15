def is_prime(number, list_of_primes):
	for prime in list_of_primes:
		if number % prime == 0:
			return False
	return True

def find_prime(number):
	primes = [2]
	prime_count = 1
	current_num = 3
	while True:
		if prime_count == number:
			return primes[-1]
		if is_prime(current_num, primes):
			primes.append(current_num)
			prime_count += 1
		current_num += 1

print find_prime(10001)
