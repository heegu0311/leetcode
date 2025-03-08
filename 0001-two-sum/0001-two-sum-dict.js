/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  const memo = new Map();

  for (let i = 0; i < nums.length; i++) {
    const needed = target - nums[i];
    if (memo.has(needed)) {
      return [memo.get(needed), i];
    }
    memo.set(nums[i], i);
  }

  return []; // No solution found
};

// Test case
console.log(twoSum([4, 1, 9, 7, 7], 14)); // [2, 3] or [2, 4]
