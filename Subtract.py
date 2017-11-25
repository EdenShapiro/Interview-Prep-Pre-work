# Definition for singly-linked list.
from math import ceil

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list

# works in quadratic time
    # def subtract(A):
    #     # count how long the linkedlist is
    #     counter = 1
    #     head = A
    #     B = A
    #     C = A
    #     while B.next:
    #         counter += 1
    #         B = B.next
    #         print B.val
    #
    #     while A.next and A.next != B:
    #         temp = A.val
    #         A.val = B.val - temp
    #         print str(A.val) + " = " + str(B.val) + " - " + str(temp)
    #
    #         A = A.next
    #         while C.next and C.next != B:
    #             C = C.next
    #         if C == A:
    #             break
    #         B = C
    #         C = A
    #         print A.val
    #         print B.val
    #         print C.val
    #         print ""
    #     if counter%2 == 0 and A.next == B:
    #         temp = A.val
    #         A.val = B.val - temp

    #
    #     A = head
    #     while A:
    #         print str(A.val) + "->",
    #         A = A.next
    #
    #     return A
        # first_node_value = A.val

    # this is a horrific monstrosity. go back and clean up
    def subtract(A):
        # count how long the linkedlist is
        counter = 1
        head = A
        B = A
        C = A
        while B.next:
            counter += 1
            B = B.next
        tail = B
        even = counter%2 == 0
        halfway = counter/2 if even else (counter/2 + 1)
        
        print "counter: " + str(counter)
        print "halfway: " + str(halfway)

        runner = 1
        while runner < halfway:
            C = C.next
            runner += 1
        mid = C
        print "mid: " + str(mid.val)

        # reverse second half of the list
        prevNode = None
        nextNode = None
        first_half_mid = C
        second_half_mid = C.next
        if even:
            C = second_half_mid
        while C != None:
            nextNode = C.next
            C.next = prevNode
            prevNode = C
            C = nextNode

        C = B # set C back to the last element of the list (instead of None)
        print "C: "+ str(C.val)
        mid.next = None
        print "mid: " + str(mid.val)
        print "mid.next: " + str(mid.next)
        print ""
        if even:
            print "list is even"
            while A and C and A != C:
                temp = A.val
                A.val = C.val - temp
                print str(A.val) + " = " + str(C.val) + " - " + str(temp)
                # if A.next == C or C.next == A:
                    # break
                A = A.next
                C = C.next
            A = first_half_mid
            C = second_half_mid
        else:
            print "list is odd"
            while A.next and C.next and A != C and A.next != C and C.next != A:
                temp = A.val
                A.val = C.val - temp
                print str(A.val) + " = " + str(C.val) + " - " + str(temp)
                A = A.next
                C = C.next

        prevNode = None
        nextNode = None
        # reverse second half again
        while B != None: # B.next and B != C:
            print B.val
            nextNode = B.next
            B.next = prevNode
            prevNode = B
            B = nextNode

        B = tail
        B.next = None
        if even:
            mid.next = C
        else:
            mid.next = C.next
        # return head
        A = head
        while A:
            print str(A.val) + "->",
            A = A.next

        # return A
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    # node6 = ListNode(6)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node4.next = node5
    # node5.next = node6
    # node6.next = None

    node5.next = None
    subtract(node1)

# Given linked list 1 -> 2 -> 3 -> 4 -> 5,
# You should return 4 -> 2 -> 3 -> 4 -> 5

# Given linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6
# You should return 5 -> 3 -> 1 -> 4 -> 5 -> 6


        # print "printing lists:"
        # while A:
        #     print str(A.val) + "->",
        #     A = A.next
        # print ""
        # while C:
        #     print str(C.val) + "->",
        #     C = C.next
