class Solution {
    public boolean isPalindrome(String s) {
        if(s.length() == 0)
            return true;
        int head = 0, tail = s.length() - 1;
        while (head < tail){
            // 如果head指针指向不是字母或数字，指针后移
            if(!Character.isLetterOrDigit(s.charAt(head))){
                head++;
            // 如果tail指针指向不是字母或数字，指针前移
            } else if(!Character.isLetterOrDigit(s.charAt(tail))){
                tail--;
            } else {
                if (Character.toLowerCase(s.charAt(head)) != Character.toLowerCase(s.charAt(tail))){
                    return false;
                }
                head++;
                tail--;
            }
        }
        return true;
    }
}
