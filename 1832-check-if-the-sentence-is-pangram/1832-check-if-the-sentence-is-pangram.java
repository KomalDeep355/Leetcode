class Solution {
    public boolean checkIfPangram(String sentence) {
        boolean [] check= new boolean[26];
        for (int i=0; i<sentence.length();i++){
            char ch = sentence.charAt(i);
            if (ch >= 'a' && ch <= 'z') {
                check[ch - 'a'] = true;
            }
        }
        for (boolean b : check) {
            if (!b) return false;
        }
    return true;
}
}