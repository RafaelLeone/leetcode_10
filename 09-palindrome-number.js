// https://leetcode.com/problems/palindrome-number/

// Input: 
const numero = 121
// Output: true
// Explicação: 121 se lê 121 da esquerda para direita e da dieita para esquerda.

let output = false

const listaDeDigitos = numero.toString().split('')
const listaReversa = [...listaDeDigitos].reverse()

if (listaDeDigitos.toString() === listaReversa.toString()) {
    output = true
}

console.log(output)
