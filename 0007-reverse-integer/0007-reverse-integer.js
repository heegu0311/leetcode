/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    let sign = x >= 0 ? 1 : -1;
    let reversed = 0;
    const MAX = Math.pow(2, 31) - 1;  // 2147483647
    const MIN = -Math.pow(2, 31);     // -2147483648
  
    reversed = Number(Math.abs(x).toString().split('').reverse().join('')) * sign;

    if(reversed > MAX || reversed < MIN) return 0;

    return reversed;
};