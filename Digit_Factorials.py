factorial = lambda num: 1 if num <= 1 else num * factorial(num-1)
factorials = [factorial(i) for i in range(10)]
def digit_fact_sum(num):
    total = 0
    while num:
        total += factorials[num%10]
        num //= 10
    return total

total = 0
# 7 digits of all 9 has a factorial power sum less than 9999999 - 7 digits is all that is needed
for i in range(3, (7 * factorial(9))+1):
    if i == digit_fact_sum(i):
        total += i
        print(i)
    
print("TOTAL:", total)