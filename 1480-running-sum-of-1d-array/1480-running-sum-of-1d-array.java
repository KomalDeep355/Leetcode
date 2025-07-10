class Solution {
    public int[] runningSum(int[] nums) {
        int [] runsum= new int [nums.length];
        if (nums.length > 0) { 
            runsum[0] = nums[0];
        }
        for (int i=1;i<nums.length;i++){
           runsum[i] = nums[i] + runsum[i - 1];
        }
        return runsum;
    }
}