def nb_year(p0, percent, aug, p):
    count = 0
    while p0 < p:
        p0 = p0 + p0 * percent * 0.01 + aug
        count = count + 1
    
    return count

print(nb_year(1500000, 2.5, 10000, 2000000))