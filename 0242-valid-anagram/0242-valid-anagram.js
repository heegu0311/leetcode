/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    // 1. 길이 체크
    if(s.length !== t.length) return false;
    // 2. count 배열 생성 (26개)
    const count = new Array(26).fill(0);
    // 3. s 순회하며 카운트 증가
    for(let i=0;i<s.length;i++) {
      const index = s[i].charCodeAt(0) - 'a'.charCodeAt(0);
      count[index]++
    }
    // 4. t 순회하며 카운트 감소 + 음수 체크
    for(let i=0;i<t.length;i++) {
      const index = t[i].charCodeAt(0) - 'a'.charCodeAt(0);
      count[index]--
      if(count[index] < 0) {
        return false;
      }
    }    
    // 5. 최종 return
    return true;
};