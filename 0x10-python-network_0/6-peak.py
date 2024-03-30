#!/usr/bin/python3
"""
Write a function that finds a peak in a list of unsorted integers.
"""


def peak_rec(arr, left, right):
    """Recursive way to find a peak"""
    if left == right:
        return arr[l]
    if right - left == 1:
        return max(arr[right], arr[left])
    m = (right + left) // 2
    if arr[m] < arr[m + 1]:
        return peak_rec(arr, m + 1, right)
    return peak_rec(arr, left, m)


def find_peak_rec(list_of_integers):
    """Function to find a peak using recursion"""
    if not list_of_integers:
        return None
    return peak_rec(list_of_integers, 0, len(list_of_integers) - 1)


def find_peak(list_of_integers):
    """Function to find a peak using binary search"""
    if not list_of_integers:
        return None
    left, right = 0, len(list_of_integers) - 1
    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return list_of_integers[left]


def find_peak_linear(list_of_integers):
    """Function to find a peak using linear search"""
    if not list_of_integers:
        return None
    for i in range(len(list_of_integers) - 1):
        if list_of_integers[i] > list_of_integers[i + 1]:
            return list_of_integers[i]
    return list_of_integers[-1]
