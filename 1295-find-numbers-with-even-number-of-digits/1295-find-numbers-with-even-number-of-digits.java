class Solution {
    public int findNumbers(int[] nums) {
        int numeven=0;
        for (int num:nums){
                int digit=0; 
                if(num==0){
                    digit=1;
                }
                else {
                    int currentnum=Math.abs(num);
                    while (currentnum > 0) {
                    currentnum /= 10;
                    digit++;
                }
            }
            if (digit%2==0){
            numeven++;
        }
        }
    return numeven;
    }
}