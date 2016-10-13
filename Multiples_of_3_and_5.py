def calculate(max):
	sum = 0
	#checks all the numbers less than than max and adds them to the sum if they are divisible by 3 or by 5
	for i in range(1, max):
		#checks to see if "i" is divisible 3 or 5
		if i % 3 == 0 or i % 5 == 0:
			sum = sum + i
	return sum

#runs calculate on 1000
print calculate(1000)
