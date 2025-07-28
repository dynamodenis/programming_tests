import java.util.HashMap;
import java.util.Map;

public class TwoSumArray {
    public static void main(String[] args) {
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        int[] result = twoSum(nums, target);

        if (result.length == 0) {
            System.out.println("No two sum solution found.");
        } else {
            System.out.println("Indices: " + result[0] + ", " + result[1]);
        }
    }

    public static int[] twoSum(int[] nums, int target) {
        // Create a hash map to store the indices of the numbers
        Map<Integer, Integer> visitedNums = new HashMap<>();
        // Iterate through the array
        for(int i = 0; i < nums.length; i++){
            int delta = target - nums[i];
            System.out.println("Delta: " + delta + ", Current Number: " + nums[i]);
            if (visitedNums.containsKey((delta))){
                System.out.println("Found a match: " + nums[i] + " + " + delta + " = " + target);
                System.out.println("Indices: " + i + ", " + visitedNums.get(delta));
                return new int[] {i, visitedNums.get(delta)};
            }
            visitedNums.put(nums[i], i);

        }

        System.out.println("visitedNums: " + visitedNums);
        return new int[0];
    }

}
