/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    for (let numero of nums2) {
        nums1.push(numero)
    }
    nums1.sort((a, b) => {
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

let nums1 = [3]
let nums2 = [-2, -1]
console.log(findMedianSortedArrays(nums1, nums2))