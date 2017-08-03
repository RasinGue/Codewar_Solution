def count_positives_sum_negatives(arr):
    count = 0
    sum = 0
    if arr ==[]:
        return arr

    for x in arr:
        if x > 0:
            count += 1
        else:
            sum += x
    
    l = [count, sum]


    return l

print(count_positives_sum_negatives([]))