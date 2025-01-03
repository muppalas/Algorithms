"searched through a SORTED array"
def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the target.
    :param arr: List of sorted elements
    :param target: Element to search for
    :return: Index of target if found, else -1
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Calculate the middle index
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1  # Search the right half
        else:
            right = mid - 1  # Search the left half

    return -1  # Target not found


# Input array (must be sorted)
arr = list(map(int, input("Enter sorted numbers separated by spaces: ").split()))
target = int(input("Enter the target number to search for: "))


result = binary_search(arr, target)

# Output 
if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found in the array.")
