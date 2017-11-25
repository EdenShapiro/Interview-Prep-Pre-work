class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def numRange(A, B, C):
        i = 0
        j = 0
        s = 0
        counter = 0 #keep track of # of sebsequences
        #when sum exceeds C, move j forward and move i back to j

        while j < len(A):
            s = A[i] + s
            if s >= B and s<= C:
                counter += 1
                i += 1
                print A[j:i]
            if s < B:
                i += 1
            if s > C or i >= len(A):
                j += 1
                i = j
                s = 0

        return counter

    # A : [10, 5, 1, 0, 2]
    # (B, C) : (6, 8)
    print numRange([10, 5, 1, 0, 2], 6, 8)
