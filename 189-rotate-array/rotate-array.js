/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    let l = nums.length;
    k = k % l;
    
    const reverse = (arr, start, end) => {
        while(start  < end){
        let temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;};
    };

    reverse(nums, 0,l-1);
    reverse(nums, 0,k-1);
    reverse(nums,k ,l-1);

    console.log(nums);

};