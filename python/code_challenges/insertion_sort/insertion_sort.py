def Insert(sorted_list, value):
    i = 0
    while value > sorted_list[i]:
        i += 1
        if i == len(sorted_list):
            break
    while i < len(sorted_list):
        temp = sorted_list[i]
        sorted_list[i] = value
        value = temp
        i += 1
    sorted_list.append(value)


def InsertionSort(input_list):
    if len(input_list) == 0:
        return []
    sorted_list = [input_list[0]]
    for i in range(1, len(input_list)):
        Insert(sorted_list, input_list[i])
    return sorted_list


if __name__ == '__main__':
    input_list = [8, 4, 23, 42, 16, 15]
    reverse_list = [20, 18, 12, 8, 5, -2]
    few_uniques = [5, 12, 7, 5, 5, 7]
    nearly_sorted = [2, 3, 5, 7, 13, 11]
    sorted_list = InsertionSort(input_list)
    sorted_reverse = InsertionSort(reverse_list)
    sorted_uniques = InsertionSort(few_uniques)
    sorted_nearly = InsertionSort(nearly_sorted)
    print(sorted_list)
    print(sorted_reverse)
    print(sorted_uniques)
    print(sorted_nearly)


