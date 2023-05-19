from movies import movies


def compare_year(a, b):
    if a["year"] > b["year"]:
        return -1
    elif a["year"] < b["year"]:
        return 1
    return 0


def merge_sort_year(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort_year(left)
    right = merge_sort_year(right)

    return merge_year(left, right, "year")


def merge_year(left, right, sort_key):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if int(left[i][sort_key]) > int(right[j][sort_key]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return [movie["title"] for movie in result]


def compare_title(a, b):
    def remove_leading_articles(title):
        articles = ["A ", "An ", "The "]
        for article in articles:
            if title.startswith(article):
                return title[len(article):]
        return title

    title_a = remove_leading_articles(a["title"])
    title_b = remove_leading_articles(b["title"])

    if title_a > title_b:
        return 1
    elif title_a < title_b:
        return -1
    return 0


def merge_sort_title(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort_title(left)
    right = merge_sort_title(right)

    return merge_title(left, right)


def merge_title(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if compare_title(left[i], right[j]) == -1:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return [movie["title"] for movie in result]


if __name__ == '__main__':
    sorted_movies_year = merge_sort_year(movies)
    print(sorted_movies_year)
    print('**************************')
    sorted_movies_title = merge_sort_title(movies)
    print(sorted_movies_title)

