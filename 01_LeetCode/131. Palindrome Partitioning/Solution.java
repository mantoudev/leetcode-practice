class Solution {
    List<List<String>> res = new ArrayList<>();

    public List<List<String>> partition(String s) {
        if(s==null||s.length()==0)
            return res;
        dfs(s,new ArrayList<String>(),0);
        return res;
    }

    public void dfs(String s,List<String> remain,int left){
        if(left==s.length()){  //判断终止条件
            res.add(new ArrayList<String>(remain));  //添加到结果中
            return;
        }
        for(int right=left;right<s.length();right++){  //从left开始，依次判断left->right是不是回文串
            if(isPalindroom(s,left,right)){  //判断是否是回文串
                remain.add(s.substring(left,right+1));   //添加到当前回文串到list中
                dfs(s,remain,right+1);  //从right+1开始继续递归，寻找回文串
                remain.remove(remain.size()-1);  //回溯，从而寻找更长的回文串
            }
        }
    }
    /**
    * 判断是否是回文串
    */
    public boolean isPalindroom(String s,int left,int right){
        while(left<right&&s.charAt(left)==s.charAt(right)){
            left++;
            right--;
        }
        return left>=right;
    }
}
