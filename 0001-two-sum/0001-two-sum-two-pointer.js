/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const n = nums.length;
    let l = 0;
    let r = n - 1;

    // Create copies of the array
    const copy = [...nums].sort((a, b) => a - b); // sort array for quick search O(n)
    const reverseCopy = [...nums].reverse(); // copy array for search O(n)

    while (l < r) {
        const sumTwo = copy[l] + copy[r];

        if (sumTwo === target) {
        const result = [
            nums.indexOf(copy[l]),
            n - 1 - reverseCopy.indexOf(copy[r]),
        ];
        result.sort((a, b) => a - b);
        return result;
        }

        if (sumTwo < target) {
        // if(target is greater than sum), move start to the next index
        l++;
        } else if (sumTwo > target) {
        // if(target is smaller than sum), move start to the prev index
        r--;
        }
    }

    // In case no solution is found
    return [];

};