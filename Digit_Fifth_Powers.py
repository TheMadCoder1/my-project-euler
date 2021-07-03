def digit_sum(num, power):
    s = 0
    while num:
        s += (num%10) ** power
        num //= 10
    return s

POWER = 5
total = 0
# 7 digits of all 9 has a fifth power sum of 6 digits - 6 digits is all that is needed
for i in range(2, (7 * 9**POWER)+1):
    if i == digit_sum(i, POWER):
        total += i
        print(i)
    
print("TOTAL:", total)