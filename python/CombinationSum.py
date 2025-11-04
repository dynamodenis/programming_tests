def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    result = []

    def dfs(start, curr, total):
        # Base call if the total of added candidates is same as traget
        if total == target:
            result.append(curr[:])
            return


        if total > target:
            return

        for i in range(start, len(candidates)):
            curr.append(candidates[i])      
            print(f"i {i} and its candicate {candidates[i]} and curr {curr} total {total}") 
            dfs(i, curr, total + candidates[i])
            curr.pop()
        

        # ---------------------------One Way ---------------------------------
        """
        # Check when you added total greater than target or the len of i >= len(candidates) you reached final and missed so retuen
        if start>= len(candidates) or total > target:
            return
        # Add current candidate to curr list
        curr.append(candidates[start])
        # Check if adding the same number can be equal to the target i.e [2,2,2,2]
        dfs(start, curr, total + candidates[start])
        curr.pop()
        # NOw call dfs again to go to the next number if same number does not work i.e [2,3,5]
        dfs(start + 1, curr, total)
        """



    dfs(0, [], 0)
    return result


"""
39. Combination Sum
Solved
Medium
Topics
premium lock iconCompanies

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the

of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:

Input: candidates = [2], target = 1
Output: []

"""