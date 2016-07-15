"""def largest_palindrome_fullarray(digits):
	max_num = int("9" * digits)
	num1 = max_num
	num2 = max_num
	array = []
	base = int("9" + ("0" * (digits - 1)))
	while num1 > base:
		while num2 > base:
			product = num1 * num2
			if is_palindrome(product):
				array.append((product, num1, num2))
			num2 -= 1
		num2 = max_num
		num1 -= 1
	print array
	array.sort()
	return array[-1]"""

def largest_palindrome_return(digits):
	max_num = int("9" * digits)
	num1 = max_num
	num2 = max_num
	base = int("9" + ("0" * (digits - 1)))
	while num1 > base:
		while num2 > base:
			product = num1 * num2
			if is_palindrome(product):
				return "%d * %d = %d (%d digits)" % (num1, num2, product, digits)
			num2 -= 1
		num2 = max_num
		num1 -= 1
	return None

def is_palindrome(num):
	if num == int(str(num)[::-1]):
		return True
	return False


print largest_palindrome_return(2)
print largest_palindrome_return(3)
print largest_palindrome_return(4)
print largest_palindrome_return(5)
print largest_palindrome_return(6)
print largest_palindrome_return(7)
print largest_palindrome_return(8)