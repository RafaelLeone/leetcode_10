// https://leetcode.com/problems/longest-common-prefix/

// Input: 
const strings = ["flower","flow","flight"]
// Output: "fl"

let dicionarioDeLetras = {}
let maiorPrefixoComum = []

for (let string of strings) {
    for (letra of string) {
        if (!(letra in dicionarioDeLetras)) {
            dicionarioDeLetras[letra] = []
        }
            dicionarioDeLetras[letra].push(string.indexOf(letra))
    }
}

for (letra in dicionarioDeLetras) {
    if (dicionarioDeLetras[letra].length === strings.length) {
        maiorPrefixoComum.push(letra)
    }
    else {
        break
    }
}

console.log(maiorPrefixoComum.join(''))
