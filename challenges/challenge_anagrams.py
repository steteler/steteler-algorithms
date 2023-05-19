def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:

        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


def is_anagram(first_string, second_string):
    first_string_list = list(first_string.lower())
    second_string_list = list(second_string.lower())

    quickSort(first_string_list)
    quickSort(second_string_list)

    first_string_anagram = "".join(first_string_list)
    second_string_anagram = "".join(second_string_list)

    if not first_string or not second_string:
        is_equal = False
    else:
        is_equal = first_string_anagram == second_string_anagram

    return (first_string_anagram, second_string_anagram, is_equal)
