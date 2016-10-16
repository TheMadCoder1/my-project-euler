def even_fibonnaci_numbers_sum(max_value):
	previous_num = 1
	current_num = 1
	num_sum = 0
	while current_num <= max_value:
		#sets the previous number to the current number and the next current number to the previous number + the current number
		current_num, previous_num = current_num + previous_num, current_num
		#checks to see if the number is even and then adds it to the total
		if current_num % 2 == 0:
			num_sum = num_sum + current_num
	return num_sum

print even_fibonnaci_numbers_sum(4000000)
