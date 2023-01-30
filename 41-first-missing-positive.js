// https://leetcode.com/problems/first-missing-positive/

// Input: 
let nums = [-5, 3]
// Output: 3
// Explicação: Os número entre [1,2] estão todos no array.

nums.sort()
let maiorNumero = Math.max(...nums)

if (maiorNumero < 1) {
    console.log(1)
}

// for (let i = 1; i <= maiorNumero + 2; ++i) { // mais 1 por precisar que o i chegue no maiorNumero e mais 1 novamente por precisar que passe do maiorNumero se necessário
//     if (!nums.includes(i)) {
//         console.log(i)
//         break
//     }
// }

let x = null

for (num of nums) {
    if (num > 0) {
        x = num
        break
    }
}

console.log(x)
