def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Hash map to store numbers and their indices
        # Key: number, Value: index
        complement_map = {}

        # Iterate through the array with index and value
        for i, num in enumerate(nums):
            complement = target - num

            # Check if the complement is already in our map
            if complement in complement_map:
                # If yes, we found the two numbers
                # Return the index of the complement and the current index
                return [complement_map[complement], i]
            else:
                # If not, add the current number and its index to the map
                # for future lookups
                complement_map[num] = i

        # According to the problem statement, there's always exactly one solution,
        # so this line should theoretically not be reached if the input is valid.
        return []
    
def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left <= right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left+1, right+1]
            
'''
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
'''