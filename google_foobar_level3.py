def zero_array_gen(size):
    zero_array = [[0]*x for x in [size]*size]
    return zero_array

print(zero_array_gen(6))