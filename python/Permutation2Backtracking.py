def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    result = []
    sol = []

    count = { n:0 for n in nums}
    # Add the nums in dict such that key is num and value is the number of nums to check for duplicates
    for i in nums:
        count[i] += 1

    print(count)


    def backtracking():
        if len(nums) == len(sol):
            result.append(sol[:])
            return

        for i in count:
            if count[i] > 0:
                sol.append(i)
                # Affter adding num in sol, reduce the number of num from dict
                count[i] -= 1 

                backtracking()
                # After backtracking is finished and return, set back the counts
                count[i] += 1
                sol.pop()


    backtracking()
    return result

"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

"""