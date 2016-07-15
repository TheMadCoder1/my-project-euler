result = 1
lst = range(2, 21)
for i in range(len(lst)):
	j = i - 1
	while j >= 0:
		if lst[i] == 1:
			break
		if lst[i] % lst[j] == 0:
			lst[i] /= lst[j]
		j -= 1
	result *= lst[i]
print result
