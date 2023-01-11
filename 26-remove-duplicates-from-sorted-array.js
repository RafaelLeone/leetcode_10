// https://leetcode.com/problems/remove-duplicates-from-sorted-array/

// Input:
let nums = [0,0,1,1,1,2,2,3,3,4]
// Output: 2, nums = [1,2,_]
// Explicação: Sua função deve retornar k = 2, com os dois primeiros elementos sendo 1 e 2 respectivamente.
// Não importa o que houver depois do k retornado (são underlines no exemplo por isso).

// int[] expectedNums = [...]; // A resposta esperada com o tamanho certo.

let k = removeDuplicatas(nums); // Chama sua implementação.

console.log(k) // assert k == listaDeNumeros.length;

function removeDuplicatas(numeros) {
    let listaDeNumeros = []
    let stringDeUnderlines = ''
    for (let numero of numeros) {
        if (!listaDeNumeros.includes(numero)) {
            listaDeNumeros.push(numero)
        }
    }
    let underlines = numeros.length - listaDeNumeros.length
    for (let i = 0; i < underlines; i++) {
        stringDeUnderlines = stringDeUnderlines + ',_'
    }
    let resultado = listaDeNumeros.length + ', nums = [' + listaDeNumeros + stringDeUnderlines + ']'
    return resultado
}
