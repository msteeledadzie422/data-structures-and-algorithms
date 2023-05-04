import pytest
from merge_sort import merge_sort


def test_merge_sort():
    input_list = [8, 4, 23, 42, 16, 15]
    expected = [4, 8, 15, 16, 23, 42]
    assert merge_sort(input_list) == expected


def test_merge_sort_reverse():
    reverse_list = [20, 18, 12, 8, 5, -2]
    expected = [-2, 5, 8, 12, 18, 20]
    assert merge_sort(reverse_list) == expected


def test_merge_sort_few_uniques():
    few_uniques = [5, 12, 7, 5, 5, 7]
    expected = [5, 5, 5, 7, 7, 12]
    assert merge_sort(few_uniques) == expected


def test_merge_sort_nearly_sorted():
    nearly_sorted = [2, 3, 5, 7, 13, 11]
    expected = [2, 3, 5, 7, 11, 13]
    assert merge_sort(nearly_sorted) == expected


def test_merge_sort_empty_list():
    input_list = []
    expected = []
    assert merge_sort(input_list) == expected


def test_merge_sort_single_element():
    input_list = [42]
    expected = [42]
    assert merge_sort(input_list) == expected
