class Solution {
    public String longestCommonPrefix(String[] strs) {
        if ( strs.length == 0){
            return "";
        }
        String prefix = strs[0];
        for (int i = 1; i < strs.length; i++){
          // 如果当前字符串不包含前缀，前缀长度-1，直到这两个字符串前缀相同，继续和后面的比较
            while (strs[i].indexOf(prefix) != 0){
                prefix = prefix.substring(0, prefix.length() - 1);
                if (prefix.isEmpty()) return "";
            }
        }
        return prefix;
    }
}
