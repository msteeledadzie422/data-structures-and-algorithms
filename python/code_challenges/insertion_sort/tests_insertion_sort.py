from insertion_sort import InsertionSort


def test_insertion_sort():
    input_list = [8, 4, 23, 42, 16, 15]
    expected = [4, 8, 15, 16, 23, 42]
    assert InsertionSort(input_list) == expected


def test_insertion_sort_reverse():
    reverse_list = [20, 18, 12, 8, 5, -2]
    expected = [-2, 5, 8, 12, 18, 20]
    assert InsertionSort(reverse_list) == expected


def test_insertion_sort_few_uniques():
    few_uniques = [5, 12, 7, 5, 5, 7]
    expected = [5, 5, 5, 7, 7, 12]
    assert InsertionSort(few_uniques) == expected


def test_insertion_sort_nearly_sorted():
    nearly_sorted = [2, 3, 5, 7, 13, 11]
    expected = [2, 3, 5, 7, 11, 13]
    assert InsertionSort(nearly_sorted) == expected


def test_insertion_sort_empty_list():
    input_list = []
    expected = []
    assert InsertionSort(input_list) == expected


def test_insertion_sort_single_element():
    input_list = [42]
    expected = [42]
    assert InsertionSort(input_list) == expected
