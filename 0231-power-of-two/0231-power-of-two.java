class Solution {
    public boolean isPowerOfTwo(int n) {
        int x=1;
        if(n<=0){
            return false;
        }
        while(n%2==0){
                n/=2;
            }
        return n==1;
    }
}