import random


def swap(first_ind: int, second_ind: int, array) -> None:
    tmp = array[first_ind]
    array[first_ind] = array[second_ind]
    array[second_ind] = tmp


def reshuffle(left_ind: int, right_ind: int, array: list) -> int:
    middle = array[(left_ind + right_ind) // 2]
    i = left_ind
    j = right_ind

    while i <= j:
        while array[i] < middle:
            i += 1

        while array[j] > middle:
            j -= 1

        if i >= j:
            break

        swap(i, j, array)
        i += 1
        j -= 1

    return j


def qsort(left_ind: int, right_ind: int, array: list):

    if left_ind < right_ind:
        new_pos = reshuffle(left_ind, right_ind, array)
        qsort(left_ind, new_pos, array)
        qsort(new_pos + 1, right_ind, array)
