def Insert(sorted, value):
    i = 0
    while value > sorted[i]:
        i += 1
        if i == len(sorted):
            break
    while i < len(sorted):
        temp = sorted[i]
        sorted[i] = value
        value = temp
        i += 1
    sorted.append(value)


def InsertionSort(input):
    sorted = [input[0]]
    for i in range(1, len(input)):
        Insert(sorted, input[i])
    return sorted



input = [8,4,23,42,16,15]
sorted = InsertionSort(input)
print(sorted)
