class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length())
            return false;
        int[] s1Array = new int[26];
        int[] s2Array = new int[26];
        // 将字符串构造成数组
        for (int i = 0; i < s1.length(); i++){
            s1Array[s1.charAt(i) - 'a']++;
            s2Array[s2.charAt(i) - 'a']++;
        }

        for (int i = 0; i < (s2.length() - s1.length()); i++){
             if(match(s1Array, s2Array)){
                 return true;
             }
            // 向右滑动窗口
            s2Array[s2.charAt(i + s1.length()) - 'a']++;
            s2Array[s2.charAt(i) - 'a']--;
        }
        // 最后比较一次
        return match(s1Array, s2Array);
    }

    boolean match(int[] s1Array, int[] s2Array){
        for (int i = 0; i < 26; i++){
            if (s1Array[i] != s2Array[i])
                return false;
        }
        return true;
    }
}
