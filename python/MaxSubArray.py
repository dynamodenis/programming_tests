def max_subarray_kadane_algorith(nums: list[int]) -> int:
    """
    Finds the contiguous subarray within an array of numbers that has the largest sum.
    Implements Kadane's Algorithm.

    Args:
        nums: A list of integers.

    Returns:
        The maximum sum of a contiguous subarray.
    """
    if not nums:
        return 0  # Or raise an error, depending on requirements for empty array

    # Initialize current_max and global_max to the first element
    # This handles cases with all negative numbers correctly (e.g., [-5, -1, -3] -> -1)
    current_max = nums[0]
    global_max = nums[0]

    # Iterate from the second element
    for i in range(1, len(nums)):
        num = nums[i]
        print(f"loop number {num}")
        # Option 1: Start a new subarray with the current number
        # Option 2: Extend the previous subarray by adding the current number
        current_max = max(num, current_max + num)

        # Update global_max if current_max is greater
        if current_max > global_max:
            print(f"Current num {num} with current max {current_max} > global_max {global_max}")
            global_max = current_max

    return global_max

# print(f"Test Case 1: [-2, 1, -3, 4, -1, 2, 1, -5, 4]")
print(f"Max Subarray Sum: {max_subarray_kadane_algorith([-2, 1, -3, 4, -1, 2, 1, -5, 4])}") # Expected: 6 ([4, -1, 2, 1])


def max_subarray_with_subarray(nums: list[int]) -> tuple[int, list[int]]:
    """
    Finds the contiguous subarray within an array of numbers that has the largest sum
    and returns both the sum and the subarray itself.
    Implements a modified Kadane's Algorithm.

    Args:
        nums: A list of integers.

    Returns:
        A tuple containing:
            - The maximum sum of a contiguous subarray.
            - The list representing the maximum sum subarray.
    """
    if not nums:
        return 0, [] # Return 0 sum and empty list for an empty input

    # Initialize current_max and global_max to the first element
    current_max = nums[0]
    global_max = nums[0]

    # Initialize indices for current_max and global_max subarrays
    # current_start: start index of the current maximum subarray
    # global_start, global_end: start and end indices of the overall maximum subarray
    current_start = 0
    global_start = 0
    global_end = 0

    # Iterate from the second element
    for i in range(1, len(nums)):
        num = nums[i]
        # Determine if we should start a new subarray or extend the current one
        if num > current_max + num:
            print(f"i {nums[i]}")

            current_max = num
            current_start = i  # New subarray starts at the current index
        else:
            current_max += num
            # current_start remains the same if we extend

        # Update global_max if current_max is greater
        if current_max > global_max:
            global_max = current_max
            global_start = current_start # Update global_start to where current_max started
            global_end = i             # Update global_end to the current index
    print(f"global start {global_start} global end {global_end}")
    return global_max, nums[global_start : global_end + 1]

# --- Test Cases ---
print(f"Test Case 1: [-2, 1, -3, 4, -1, 2, 1, -5, 4]")
# sum1, subarray1 = max_subarray_with_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# print(f"Max Subarray Sum: {sum1}, Subarray: {subarray1}") # Expected: Sum: 6, Subarray: [4, -1, 2, 1]
