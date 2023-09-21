def binary_search(array, target):
    """
    Performs a binary search on the given array to find the target element.

    Args:
        array: A sorted array of elements.
        target: The element to search for.

    Returns:
        The index of the target element in the array, or -1 if the target element is not found.
    """

    low, high = 0, len(array) - 1

    while low <= high:
        """
        Keep searching until the low and high pointers meet.
        """

        mid = (low + high) // 2

        if array[mid] == target:
            """
            If the target element is found, return its index.
            """
            return mid
        elif array[mid] < target:
            """
            If the target element is greater than the middle element,
            set the low pointer to the middle element plus one.
            """
            low = mid + 1
        else:
            """
            If the target element is less than the middle element,
            set the high pointer to the middle element minus one.
            """
            high = mid - 1

    return -1


def main():
    """
    The main function.
    """

    array = [1, 3, 5, 7, 9]
    target = 7

    result = binary_search(array, target)

    if result != -1:
        print(f"The target element is at index {result}")
    else:
        print("The target element is not in the array")


if __name__ == "__main__":
    main()
