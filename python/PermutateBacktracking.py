def permute(self, nums: List[int]) -> List[List[int]]:
    result = []
    sol = []

    def backtracking():
        if len(sol) == len(nums):
            result.append(sol[:])
            return

        for i in nums:
            if i not in sol:
                sol.append(i)
                backtracking()
                sol.pop()

        return result
    backtracking()
    return result

"""
Given an array nums of distinct integers, return all the possible

. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]

"""