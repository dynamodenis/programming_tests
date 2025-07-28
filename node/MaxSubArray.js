function maxSubArray(nums) {
    if (nums.length === 0) return 0;

    let maxSoFar = nums[0];
    let maxEndingHere = nums[0];

    for (let i = 1; i < nums.length; i++) {
        console.log(`Before Current number: ${nums[i]}, Max ending here: ${maxEndingHere}, Max so far: ${maxSoFar}`);

        maxEndingHere = Math.max(nums[i], maxEndingHere + nums[i]);
        console.log(`After Current number: ${nums[i]}, Max ending here: ${maxEndingHere}, Max so far: ${maxSoFar}`);

        // Update the maximum subarray sum found so far
        // by comparing the current maximum ending here with the overall maximum
        // This ensures we always have the largest sum of any contiguous subarray
        // at any point in the iteration.
        maxSoFar = Math.max(maxSoFar, maxEndingHere);
    }

    return maxSoFar;
}

// Example usage:
const nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4];
const result = maxSubArray(nums);
console.log(`Maximum subarray sum is: ${result}`); // Output: 6 (