/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    const rows = Array(numRows).fill('')
    let currRow = 0;
    let direction = 1;

    if(s.length === 1 || numRows === 1) {
        return s;
    }

    for (let i=0;i<s.length;i++) {
        rows[currRow] += s[i];
        
        if(currRow === 0) {
            direction = 1;
        }
        if(currRow === numRows - 1) {
            direction = -1;
        }
        currRow += direction;
    }

    return rows.join('');
};

// PAYPALISHIRING 5
// P       H
// A     S I
// Y   I   R
// P L     I G
// A       N