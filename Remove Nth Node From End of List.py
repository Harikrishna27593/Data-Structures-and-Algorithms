# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return head
        else:
            ptr3=ListNode(0)
            ptr3.next=head
            ptr1=ptr3
            ptr2=ptr3
        for i in range(n):
            ptr1=ptr1.next
        while(ptr1.next!=None):
            ptr1=ptr1.next
            ptr2=ptr2.next
            
        ptr2.next=ptr2.next.next
        return ptr3.next

def stringToIntegerList(input):
    input = input.strip()
    input = input[1:-1]
    return [int(number) for number in input.split(",")]

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return result[:-2]

import sys
def readlines():
    for line in sys.stdin:
        yield line.strip('\n')

def main():
    lines = readlines()
    while True:
        try:
            line = lines.next()
            head = stringToListNode(line)
            line = lines.next()
            n = int(line)
            
            ret = Solution().removeNthFromEnd(head, n)

            out = listNodeToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()