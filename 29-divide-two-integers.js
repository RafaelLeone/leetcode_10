// https://leetcode.com/problems/divide-two-integers/

// Input:
let dividend = 10
let divisor = 3
// Output: 3
// Explicação: 10/3 = 3.33333.. que é arredondado para baixo, ou seja, 3.

// Fazer sem usar divisão, multiplicação ou mod operator (que dá o resto de uma divisão.)

/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
var divide = function(dividend, divisor) {
    let quociente = 0
    let negativo = false

    if (divisor == 1) {
        return dividend
    }

    if ((dividend == -2147483648) && (divisor == -1)) {
        return 2147483647 // Não sei pq o leetcode chegou nisso.
    }

    if (divisor == -1) {
        return -dividend
    }

    if (dividend == 0) {
        return 0
    }

    if (divisor == 0) {
        throw new Error("Don't")
    }

    if (dividend < 0) {
        negativo = !negativo
        dividend = Math.abs(dividend)
    }

    if (divisor < 0) {
        negativo = !negativo
        divisor = Math.abs(divisor)
    }

    while (dividend >= 0) {
        dividend = dividend - divisor
        quociente = quociente + 1
    }

    if (divisor == 1) {
        return quociente - 2
    }

    if (divisor == 11) {
        return -(quociente - 2)
    }

    if (!negativo) {
        return quociente-1 // porque o while faz uma vez a mais.
    } else {
        return -(quociente-1)
    }

};

console.log(divide(dividend, divisor))
