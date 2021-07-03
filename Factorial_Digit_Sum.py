# TODO: Find more efficient sol that doesn't rely on big number maybe?
factorial = lambda num: 1 if num == 1 else factorial(num-1) * num
print(sum([int(char) for char in str(factorial(100))]))