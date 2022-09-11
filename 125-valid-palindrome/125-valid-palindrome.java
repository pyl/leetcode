class Solution {
    public boolean isPalindrome(String s) {
        int l = 0;
        int r = s.length();
        
        while (l < r){
            if (!Character.isLetterOrDigit(s.charAt(l))) {
                l += 1;
                continue;
            }
            System.out.println(l);
            System.out.println(r);
            if (!Character.isLetterOrDigit(s.charAt(r-1))) {
                r -= 1;
                continue;
            }
            if (Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r-1))) {
                return false;
            }
            l += 1;
            r -= 1;
        }
        return true;
    }
}