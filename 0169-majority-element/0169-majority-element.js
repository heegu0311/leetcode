/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let candidate = 0;
    let count = 0;
  
    for(let num of nums) {
        if(count === 0) {
            candidate = num;
            count = 0;
        }

        if(num === candidate) {
            count++;
        } else {
            count--;
        }

        if(count > nums.length / 2) {
            return candidate;
        }
    }

    return candidate;
};