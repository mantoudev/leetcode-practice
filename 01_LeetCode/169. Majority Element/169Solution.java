class Solution {
    public int majorityElement(int[] nums) {
        int count = 1;
        int temp = nums[0];
        for(int i = 1; i < nums.length; i++){
            if(temp == nums[i]){
                count++;
            } else {
                count--;
                if(count == 0){
                    temp = nums[i+1];
                }
            }
        }
        return temp;
    }
}
