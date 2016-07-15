def squares(max_num):
	i = 1
	sum = 0
	while i <= max_num:
		sum += i ** 2
		i += 1
	return sum

def sum_squared(max_num):
	return sum(range(1, max_num + 1)) ** 2

def compute_diff(max_num):
	return sum_squared(max_num) - squares(max_num)

print compute_diff(100)
