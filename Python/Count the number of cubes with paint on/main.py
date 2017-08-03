def count_squares(cuts):
    return (cuts + 1) ** 3 - (cuts -1 ) ** 3

print(count_squares(5))