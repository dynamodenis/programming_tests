def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    steps = 0  # to visualize how many steps it takes

    while left <= right:
        steps += 1
        mid = (left + right) // 2
        guess = arr[mid]

        if guess == target:
            print(f"✅ Found {target} at index {mid} in {steps} steps")
            return mid

        elif guess < target:
            left = mid + 1  # search in the right half
        else:
            right = mid - 1  # search in the left half

    print(f"❌ {target} not found (took {steps} steps)")
    return -1


# Example usage
arr = list(range(1, 129))  # sorted list of 128 elements
binary_search(arr, 77)


# ---------------------34. Find First and Last Position of Element in Sorted Array-----------------------------
"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

"""
def searchRange(self, nums: List[int], target: int) -> List[int]:
    left  = self.binarySearch(nums, target, True)
    right  = self.binarySearch(nums, target, False)

    return [left, right]

def binarySearch(self, nums, target, leftBias):
    left, right = 0, len(nums) -1

    i = -1
    while left <= right:
        mid = (left + right) // 2
        curr = nums[mid]                

        if curr < target:
            left = mid + 1
        elif curr > target:
            right = mid - 1
        else:
            print(f"curr {curr} target {target} and coordinates left {left} right {right} and mid {mid}")
            i = mid

            if leftBias:
                # means move further from right to left
                right = mid -1
            else:
                left = mid + 1

    return i




# -------------------------------------33. Search in Rotated Sorted Array--------------------------------------------

"""
33. Search in Rotated Sorted Array
Solved
Medium
Topics
premium lock iconCompanies

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:

Input: nums = [1], target = 0
Output: -1

"""
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            curr = nums[mid]

            if curr == target:
                return mid

            # left portion
            if nums[left] <= curr:
                # If it on the left porting but it need to be on the right portion
                if target > curr or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid -1

            else:
                if target < curr or target > nums[right]:
                    right = mid -1 
                else:
                    left = mid + 1

        return -1