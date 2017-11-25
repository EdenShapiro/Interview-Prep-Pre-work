
# def longestConsecutive(A):
#     longest = 0
#     hashmap = {}
#
#     for ele in A:
#         if ele not in hashmap:
#             hashmap[ele] = 0
#         elif ele - 1 not in hashmap:
#             current = ele
#             current_longest = 1
#             while current + 1 in hashmap:
#                 current += 1
#                 current_longest += 1
#             longest = max(longest, current_longest)
#
#     return longest

# print longestConsecutive([6, 4, 5, 2, 3])
                        # 1 #1 #3 #1 #3


def longestConsecutive(A):
    hashmap = {}
    for ele in A:
        if ele not in hashmap:
            new_tail = hashmap[ele - 1][0] if (ele - 1) in hashmap else ele
            new_head = hashmap[ele + 1][1] if (ele + 1) in hashmap else ele
            new_length = new_head - new_tail + 1

            hashmap[new_tail] = (new_tail, new_head, new_length)
            hashmap[new_head] = (new_tail, new_head, new_length)

    return max(hashmap.values(), key=lambda x: x[2])[2]

print longestConsecutive([6, 4, 5, 2, 3])
