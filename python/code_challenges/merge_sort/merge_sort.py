def merge_sort(arr):
    n = len(arr)

    if n > 1:
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        merge(left, right, arr)

    return arr


def merge(left, right, arr):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


if __name__ == '__main__':
    input_list = [8, 4, 23, 42, 16, 15]
    reverse_list = [20, 18, 12, 8, 5, -2]
    few_uniques = [5, 12, 7, 5, 5, 7]
    nearly_sorted = [2, 3, 5, 7, 13, 11]
    sorted_list = merge_sort(input_list)
    sorted_reverse = merge_sort(reverse_list)
    sorted_uniques = merge_sort(few_uniques)
    sorted_nearly = merge_sort(nearly_sorted)
    print(sorted_list)
    print(sorted_reverse)
    print(sorted_uniques)
    print(sorted_nearly)
