class Solution {
    public int smallestRangeI(int[] nums, int k) {
        int minVal = Integer.MAX_VALUE;
        int maxVal = Integer.MIN_VALUE;
        
        for (int num : nums) {
            minVal = Math.min(minVal, num);
            maxVal = Math.max(maxVal, num);
        }
        
        int newMin = minVal + k;
        int newMax = maxVal - k;
        
        return Math.max(0, newMax - newMin);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        
        int[] nums1 = {1};
        System.out.println(sol.smallestRangeI(nums1, 0)); 

        int[] nums2 = {0, 10};
        System.out.println(sol.smallestRangeI(nums2, 2)); 

        int[] nums3 = {1, 3, 6};
        System.out.println(sol.smallestRangeI(nums3, 3)); 
    }
}
