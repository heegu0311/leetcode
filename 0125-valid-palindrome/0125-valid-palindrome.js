/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
  const isAlphanumeric = (char) => {
    const lower = char.toLowerCase();
    return (lower >= 'a' && lower <= 'z') || (lower >= '0' && lower <= '9');
  };
  
  let left = 0;
  let right = s.length - 1;
  
  while (left < right) {
    if (!isAlphanumeric(s[left])) {
        left++;
        continue;
    }
    if (!isAlphanumeric(s[right])) {
        right--;
        continue;
    }

    if (s[left].toLowerCase() !== s[right].toLowerCase()) return false;
    left++;
    right--;
  }
  
  return true;
};