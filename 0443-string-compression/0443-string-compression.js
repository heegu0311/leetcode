/**
 * @param {character[]} chars
 * @return {number}
 */
var compress = function(chars) {
    let i = 0;
    let write = 0;

    while (i < chars.length) {
        const currentChar = chars[i];
        let count = 0;

        while (chars[i] === currentChar && i < chars.length) {
            count++;
            i++;
        }

        chars[write] = currentChar;
        write++;

        if(count > 1) {
            for (let num of String(count).split('')) {
                chars[write] = num;
                write++;
            }
        }
    }
    
    return write;
};