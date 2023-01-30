// https://leetcode.com/problems/palindrome-number/

// Input: 
const x = 121
// Output: true
// Explicação: 121 se lê 121 da esquerda para direita e da dieita para esquerda.

// Copiar a partir daqui para o site:
/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let output = false

    const listaDeDigitos = x.toString().split('')
    const listaReversa = [...listaDeDigitos].reverse()

    if (listaDeDigitos.toString() === listaReversa.toString()) {
        output = true
    }

    return output
};
// Não copiar no site:
console.log(isPalindrome(x))
