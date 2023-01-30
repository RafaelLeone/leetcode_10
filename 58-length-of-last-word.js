// https://leetcode.com/problems/length-of-last-word/

// Input:
let s = "   fly me   to   the moon  "
// Output: 4
// Explicação: 'moon' é a última palavra e tem 4 letras. 

// Copiar a partir daqui para o site em JavaScript:
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let listaDePalavras = s.split(' ')
    let ultimaPalavra = listaDePalavras.length - 1
    while (true) {
        if (listaDePalavras[ultimaPalavra] == '') {
            listaDePalavras.splice(ultimaPalavra, 1)
            ultimaPalavra = listaDePalavras.length - 1
        } else { break }
    }

    return listaDePalavras[ultimaPalavra].length
};
// Não copiar para o site:
console.log(lengthOfLastWord(s))
