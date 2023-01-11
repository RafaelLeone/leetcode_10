// https://leetcode.com/problems/divide-two-integers/

// Input:
let dividendo = 10
let divisor = 3
// Output: 3
// Explicação: 10/3 = 3.33333.. que é arredondado para baixo, ou seja, 3.

// Fazer sem usar divisão, multiplicação ou mod operator (que dá o resto de uma divisão.)

let quociente = 0
let negativo = false

if (divisor == 0) {
    throw new Error("Don't")
}

if (dividendo < 0) {
    negativo = !negativo
    dividendo = Math.abs(dividendo)
}
if (divisor < 0) {
    negativo = !negativo
    divisor = Math.abs(divisor)
}

while (dividendo >= 0) {
    dividendo = dividendo - divisor
    quociente = quociente + 1
}

if (!negativo) {
    console.log(quociente -1) // porque o while faz uma vez a mais.
} else {
    console.log(-(quociente -1))
}
