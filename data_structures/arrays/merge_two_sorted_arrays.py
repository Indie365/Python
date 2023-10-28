"""
    https://en.wikipedia.org/wiki/Merge_algorithm
"""


def merge_two_sorted_arrays(nums1: list[any], nums2: list[any]) -> list[any]:
    """
    Merge two sorted arrays.

    Args:
        nums1: The first array.
        nums2: The second array.

    Returns:
        The merged sorted array.

    Examples:
        >>> merge_two_sorted_arrays([1, 5, 7], [0, 4, 9])
        [0, 1, 4, 5, 7, 9]

        >>> merge_two_sorted_arrays([-11, 5, 45], [0, 5, 9])
        [-11, 0, 5, 5, 9, 45]

        >>> merge_two_sorted_arrays([-11, 5, 45], [0, 5.5, 9])
        [-11, 0, 5, 5.5, 9, 45]

        >>> merge_two_sorted_arrays(['a', 'c', 'e'], ['b', 'd',  'f'])
        ['a', 'b', 'c', 'd', 'e', 'f']

        >>> merge_two_sorted_arrays([], [])
        []

        >>> merge_two_sorted_arrays([6, 2, 1], [10, 23, -11])
        Traceback (most recent call last):
        ...
        ValueError: The array is not sorted

    """

    if nums1 != sorted(nums1) or nums2 != sorted(nums2):
        raise ValueError("The array is not sorted")

    # Initialize two pointers and an array to store the merged array.
    i, j = 0, 0
    merged = []

    # Merge the two arrays
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    # Merge remaining elements
    while i < len(nums1):
        merged.append(nums1[i])
        i += 1

    # Merge remaining elements
    while j < len(nums2):
        merged.append(nums2[j])
        j += 1

    return merged


if __name__ == "__main__":
    import doctest

    doctest.testmod()