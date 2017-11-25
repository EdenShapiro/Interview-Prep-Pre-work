
# Given an array, find the next greater element G[i] for every element A[i] in the array. The Next greater Element for an element A[i] is the first greater element on the right side of A[i] in array.
# Elements for which no greater element exist, consider next greater element as -1.

# Input : A : [3, 2, 1]
# Output : [-1, -1, -1]

# Input : A : [4, 5, 2, 3, 10]
# Output : [5, 10, 3, 10, -1]

# Input : A : [4, 5, 2, 3, 10]
# Output : [5, 10, 3, 10, -1]

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(A):
        i = 0
        j = 1
        answer_arr = [0] * len(A)
        while i < len(A):
            while j < len(A) and A[j] <= A[i]:
                j += 1
            if j >= len(A):
                answer_arr[i] = -1
            else:
                answer_arr[i] = A[j]
            i += 1
            j = i + 1

        return answer_arr



    print nextGreater([3, 2, 1])
    print nextGreater([4, 5, 2, 3, 10])
    print nextGreater([4, 5, 2, 10])
