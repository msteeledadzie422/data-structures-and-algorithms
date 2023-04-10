def zip_lists(list1, list2):
    if list1.head is None:
        return list2
    if list2.head is None:
        return list1

    result = LinkedList()
    current1 = list1.head
    current2 = list2.head

    while current1 is not None and current2 is not None:
        result.append(current1.value)
        result.append(current2.value)
        current1 = current1.next
        current2 = current2.next

    while current1 is not None:
        result.append(current1.value)
        current1 = current1.next

    while current2 is not None:
        result.append(current2.value)
        current2 = current2.next

    return result

