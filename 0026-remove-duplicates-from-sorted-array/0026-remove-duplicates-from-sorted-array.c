int removeDuplicates(int* nums, int numsSize) {
    if (numsSize == 0){
        return 0;
    }
    int write_index = 1;
    for (int i = 1; i < numsSize; i++){
        if(nums[i] != nums[i - 1]){
            nums[write_index] = nums[i];
            write_index++;
        }
    }

    return write_index;
}