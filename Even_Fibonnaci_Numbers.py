def even_fibonnaci_numbers_sum(max_value):
	previous_num = 1
	current_num = 1
	num_sum = 0
	while current_num <= max_value:
		current_num, previous_num = current_num + previous_num, current_num
		if current_num % 2 == 0:
			num_sum = num_sum + current_num
	return num_sum

print even_fibonnaci_numbers_sum(4000000)