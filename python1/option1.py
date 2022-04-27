i = 30
while i <= 60:
    j = 2
    isPrime = False
    
    while j < i:
        if i % j == 0:
            break
        j +=1
    
    if j == i:
        isPrime = True
    
    if isPrime:
        print('Prime')
    else:
        print(i)
    
    i += 1