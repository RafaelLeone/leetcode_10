// https://leetcode.com/problems/longest-common-prefix/

// Input: 
const strs = ["flower", "flight"]
// Output: "fl"

// Copiar a partir daqui para o site:
/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    let maiorPrefixoComum = []

    for (letra of strs[0]) {
        maiorPrefixoComum.push(letra)
    }

    if (strs.length == 0) {
        return maiorPrefixoComum
    }

    strs.splice(0, 1)

    for (palavra of strs) {
        for (index in maiorPrefixoComum) {
            if (palavra[index] == maiorPrefixoComum[index]) {
                continue
            }
            maiorPrefixoComum.splice(index, maiorPrefixoComum.length)
        }
    }

    return maiorPrefixoComum.join('')
};
// Não copiar para o site:
console.log(longestCommonPrefix(strs))
