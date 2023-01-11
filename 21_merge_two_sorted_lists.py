# https://leetcode.com/problems/merge-two-sorted-lists/

# Input: 
list1 = [1, 2, 4]
list2 = [1, 3, 4]
# Output: [1,1,2,3,4,4]

for elemento in list2:
    list1.append(elemento)

list1.sort()

print(list1)
