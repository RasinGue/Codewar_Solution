def dig_pow(n, p):
    string = str(n)
    lst = list(string)
    sum = 0
    count = p

    for x in lst:
        sum += int(x) ** count
        count += 1
    
    if sum % n == 0:
        return int(sum / n)
    else:
        return -1

print(dig_pow(46288, 3))