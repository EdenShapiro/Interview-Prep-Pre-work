import sys
import heapq

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    # def kthsmallest(A, k):
    #     return sorted(A)[k-1]

    def kthsmallest(A, k):
        k_array = [sys.maxint] * k
        heapq.heapify(k_array)
        for index, element in enumerate(A):
            for i in range(len(k_array)):
                if element < k_array[i]:
                    heapq.heappush(k_array, element)
                    # k_array.insert(i, element)
                    k_array.pop()
                    break
        print k_array
        return k_array[k-1]


    print kthsmallest([2, 1, 4, 3, 2], 3)


# A : [2 1 4 3 2]
# k : 3
#
# answer : 2
