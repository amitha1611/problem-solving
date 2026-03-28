class Solution {
    public int minCostToMoveChips(int[] nums) {
        int even=0,odd=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]%2==0){
                even++;
            }
            else{
                odd++;
            }
        }
        if(even<odd){
            return even;
        }
        else{
            return odd;
        }
    }
}
