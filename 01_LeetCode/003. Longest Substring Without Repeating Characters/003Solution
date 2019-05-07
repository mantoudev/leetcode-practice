class Solution {
    public int lengthOfLongestSubstring(String s) {
        int length = s.length();
        int maxStrLength = 0, i = 0, j = 0;
        Set<Character> str = new HashSet<>();
        while (i < length && j < length){
            if (!str.contains(s.charAt(j))){
                str.add(s.charAt(j++));
                maxStrLength = Math.max(maxStrLength, j - i);
            } else {
                str.remove(s.charAt(i++));
            }
        }
        return maxStrLength;
    }
}
