#!python


def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if array[index] == item:
        return index
    elif index >= len(array)-1:
        return None
    return linear_search_recursive(array, item, index+1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):

    # initialize some variables
    left = 0
    right = len(array)-1
    mid = right // 2

    # loop until we find the index or base case is hit
    # each iteration, we set left or right index and update mid
    # depending on if mid if greater or less than item
    while left <= right:
        if array[mid] == item:
            return mid
        elif array[mid] < item:
            left = mid + 1
        else:
            right = mid - 1
        mid = left + (right - left) // 2

    # base case - item was not found, return None
    return None


def binary_search_recursive(array, item, left=None, right=None):

    # initialize left and right on first iteration
    if left is None:
        left, right = 0, len(array)-1

    # base case - if item is not found, return None
    if right < left:
        return None

    # find the middle index / partitioning index
    mid = left + (right-left) // 2

    # if the middle element is item, return middle index.
    # otherwise continue searching on the appropriate side
    if array[mid] == item:
        return mid
    elif array[mid] < item:
        return binary_search_recursive(array, item, mid+1, right)
    return binary_search_recursive(array, item, left, mid-1)
