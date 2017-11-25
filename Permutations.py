# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
# [1,1,2] has the following unique permutations:

# [1,1,2]
# [1,2,1]
# [2,1,1]


# class Solution:
    # @param A : list of integers
    # @return a list of list of integers

def permute(A):

    def permute_helper(A):
        if len(A) == 0:
            return [[]]
        permutations = []
        for i, a in enumerate(A):
            list_permutations = permute(A[i+1:] + A[:i])
            permutations.extend([[a] + p for p in list_permutations])
        return permutations

    return uniqueify(permute_helper(A))

def uniqueify(k):
    kt = [tuple(i) for i in k]
    kt_deduped = list(set(kt))
    return [list(i) for i in kt_deduped]

print uniqueify([[1, 1, 3],
        [1, 3, 1],
[1, 3, 1],
[1, 1, 3],
[3, 1, 1],
[3, 1, 1]])


print len(permute([1])) == 1
print len(permute([1, 2])) == 2
print len(permute([1, 1, 3])) == 3
print len(permute([1, 2, 3, 4])) == 24
print len(permute([1, 2, 3, 4, 5])) == 120

for p in permute([1, 1, 3]):
    print p
