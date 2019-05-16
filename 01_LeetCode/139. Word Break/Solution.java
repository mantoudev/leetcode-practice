class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        int len = s.length();
        int max_len = 0;
        boolean[] result = new boolean[len + 1];
        // 最大单词长度
        for (String temp : wordDict){
            if (temp.length() > max_len)
                max_len = temp.length();
        }
        // 遍历字符串, 从第一个字母开始，依次往后，判断是否可拆分
        for (int i = 1; i < len; i++){
            // 从 j 到 i 是否可拆分
            for (int j = i - 1; j >= 0 && i - j <= max_len; j--){
               //1. 如果0-j不可拆分，j-i也不可拆分 ； 2. 如果0-j可拆分，判断j-i是否包含在字典中
                if (result[j] && wordDict.contains(s.substring(j, i)))
                    result[i] = true;
                    break;
            }
        }
        return result[len];
    }
}
