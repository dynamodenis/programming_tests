def subsets(nums: list[int]):
    n = len(nums)
    
    response, current = [], []
    
    def backtrack(i):
        if i == n:
            response.append(current[:]) # create a shallow copy of current[:] since its a shared mutable object so we need a copy to avoid it being affected ny pop and appends
            print(f"Current num {i} with current array {current}")
            return
        
        # Dont pick nums[i], "Exclude nums[i]" choice. meaning going down the tree
        backtrack(i+1)
        
        # Use the current num, Include nums[i] in the current subset, meaning going up the tree after
        current.append(nums[i])
        backtrack(i+1)
        current.pop() # remove the last added number this is where backtracking works
    
    backtrack(0)
    print(f"Response {response}")
    return response

subsets([1,2,3])

#Response [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]