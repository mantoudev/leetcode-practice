class Solution {
    public int majorityElement(int[] nums) {
        int count = 0;
        Integer temp = null;
        for(int num : nums){
            if (count == 0){
                temp = num;
            }
            count += (num == temp) ? 1 : -1;
        }
        return temp;
    }
}
