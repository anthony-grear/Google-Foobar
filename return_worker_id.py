def solution(x, y):
    nested_list = []
    c_index_values = [n**2-3*n+2 for n in range(1,1001)]
    b_counter = 1
    length_counter = 1001
    c_counter = 0
    while length_counter>1:
        list_maker = [int(0.5*(n**2 + (b_counter)*n + c_index_values[c_counter])) for n in range(1, length_counter)]
        nested_list.append(list_maker)
        b_counter +=2
        c_counter +=1
        length_counter -=1
    return str(nested_list[y-1][x-1])

print(solution(3,2))