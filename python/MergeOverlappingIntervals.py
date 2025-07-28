def merge_intervals(intervals):
    """
    Merges overlapping intervals in a list and returns a new list of non-overlapping intervals.

    Args:
        intervals: A list of lists, where each inner list represents an interval [start, end].
                   Example: [[1,3], [2,6], [8,10], [15,18]]

    Returns:
        A list of merged, non-overlapping intervals.
    """
    if not intervals:
        return []

    # 1. Sort the intervals by their start times.
    # If start times are equal, sort by end times (optional but good practice for consistency).
    intervals.sort(key=lambda x: x[0])

    # 2. Initialize the result list with the first interval
    merged = [intervals[0]]

    # 3. Iterate through the rest of the intervals
    for current_start, current_end in intervals[1:]:
        # Get the last merged interval from the result list
        last_merged_start, last_merged_end = merged[-1]

        # Check for overlap: current_start is less than or equal to the end of the last merged interval
        if current_start <= last_merged_end:
            # Overlap! Merge by extending the end of the last merged interval
            # The new end is the maximum of the current interval's end and the last merged interval's end
            merged[-1][1] = max(last_merged_end, current_end)
        else:
            # No overlap. Add the current interval as a new, separate interval
            merged.append([current_start, current_end])

    return merged

# --- Test Cases ---
print(f"Test Case 1: [[1,3], [2,6], [8,10], [15,18]] -> {merge_intervals([[1,3], [2,6], [8,10], [15,18]])}")
# Expected: [[1, 6], [8, 10], [15, 18]]

print(f"Test Case 2: [[1,4], [4,5]] -> {merge_intervals([[1,4], [4,5]])}")
# Expected: [[1, 5]] (intervals touching at the boundary are considered overlapping and merge)

print(f"Test Case 3: [[1,4], [0,4]] -> {merge_intervals([[1,4], [0,4]])}")
# Expected: [[0, 4]]

print(f"Test Case 4: [[1,4], [0,0]] -> {merge_intervals([[1,4], [0,0]])}")
# Expected: [[0, 0], [1, 4]] (order after sort, then no merge)

print(f"Test Case 5: [[1,4], [0,1]] -> {merge_intervals([[1,4], [0,1]])}")
# Expected: [[0, 4]]

print(f"Test Case 6: [[1,4], [0,1], [3,5]] -> {merge_intervals([[1,4], [0,1], [3,5]])}")
# Sorted: [[0,1], [1,4], [3,5]]
# Expected: [[0, 5]]

print(f"Test Case 7: [[1,3]] -> {merge_intervals([[1,3]])}")
# Expected: [[1, 3]]

print(f"Test Case 8: [] -> {merge_intervals([])}")
# Expected: []

print(f"Test Case 9: [[2,3],[4,5],[6,7],[8,9],[1,10]] -> {merge_intervals([[2,3],[4,5],[6,7],[8,9],[1,10]])}")
# Sorted: [[1,10], [2,3], [4,5], [6,7], [8,9]]
# Expected: [[1, 10]]