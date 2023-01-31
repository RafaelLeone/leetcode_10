// https://leetcode.com/problems/median-of-two-sorted-arrays/

//Input: 
let nums1 = [1,3]
let nums2 = [2]
// Output: 2.00000
// Explanation: merged array = [1,2,3] and median is 2.

// Copiar a partir daqui para o site em JavaScript:
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    for (let numero of nums2) {
        nums1.push(numero)
    }
    nums1.sort((a, b) => { //para os casos negativos, o js não ordena sozinho.
        if (a < b) {
          return -1;
        }
        if (a > b) {
          return 1;
        }
        return 0;
    })
    if ((nums1.length%2) > 0) {
        console.log(nums1)
        return nums1[Math.round((nums1.length/2)-1)]
    } else {
        return ((nums1[(nums1.length/2)-1])+(nums1[(nums1.length/2)]))/2
    }
};
// Não copiar no site:
console.log(findMedianSortedArrays(nums1, nums2))
