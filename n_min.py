def n_min(lst = [], n = 1):
    lst.sort()
    temp_min_1 = temp_min_2 = lst[0]

    for i in range(1, n):
        temp_min_1 *= lst[i]
    for i in range(len(lst) - 1, len(lst) - n, -1):
        temp_min_2 *= lst[i]

    print(f"{temp_min_1} {temp_min_2}")
    n_min = min(temp_min_1, temp_min_2)

    return n_min

    