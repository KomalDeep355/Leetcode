class Solution {
    public int maximumWealth(int[][] accounts) {
        int maxwealth=0;
        for (int i=0;i<accounts.length;i++){
            int curcustomerwealth=0;
            for (int j=0;j<accounts[i].length;j++){
                curcustomerwealth+=accounts[i][j];
            }
            if(curcustomerwealth>maxwealth){
            maxwealth=curcustomerwealth;
        }
        }
        return maxwealth;
    }
}