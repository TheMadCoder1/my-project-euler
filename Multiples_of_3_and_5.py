# def calculate(max):
# 	sum = 0
# 	#checks all the numbers less than than max and adds them to the sum if they are divisible by 3 or by 5
# 	for i in xrange(1, max+1):
# 		print(i)
# 		#checks to see if "i" is divisible 3 or 5
# 		if i % 3 == 0 or i % 5 == 0:
# 			sum = sum + i
# 	return sum

def sum_divisible_by(target, n):
	div = target // n
	return n * div * (div+1) // 2

def calculate(target):
	return sum_divisible_by(target, 3) + sum_divisible_by(target, 5) - sum_divisible_by(target, 15)

target = 1000000000-1
print calculate(target)
