from math import sqrt

def get_num_divisors(num):
    sq = int(sqrt(num))
    divs = 2
    for i in range(2, sq+1):
        if num % i == 0:
            divs += 2
    return divs




cur = 0

i = 1
while True:
    cur += i
    num_divisors = get_num_divisors(cur)
    # print(i, cur, num_divisors)
    if num_divisors > 500:
        print(cur)
        print(num_divisors)
        exit()
    i += 1