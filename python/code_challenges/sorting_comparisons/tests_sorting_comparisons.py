from movies import movies
from sorting_comparisons import merge_sort_year, merge_sort_title


def test_merge_sort_year():
    input_list = movies
    expected = ["The Intouchables", "Valkyrie", "Stardust", "Ratatouille", "City of God", "Memento", "The Shawshank Redemption", "Beetlejuice", "Crocodile Dundee", "The Cotton Club"]
    assert merge_sort_year(input_list) == expected
