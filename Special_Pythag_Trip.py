for i in range(3, 1000/3):
    for j in range(i, (1000-i)/2):
        k = 1000 - i - j
        if i**2+j**2 == k**2:
            print i*j*k
            exit(0)