# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        first=head
        second=head
        c=head
        count=0
        p=0
        while c is not None:
            c=c.next
            p=p+1
        if k==0 or p==k:
            return head
        else:
            if head is not None and head.next is not None and k<p:
                   while first is not None and first.next is not None:
                      if count>=k:
                        second=second.next
                        first=first.next
                      else:
                        count=count+1
                        first=first.next
        
                   first.next=head
        
        
                   head=second.next
                   second.next= None
                   return head
            
            
            elif k>p and p!=0:
                j=k%p
                k=j
                if head is not None and head.next is not None and k<p:
                   while first is not None and first.next is not None:
                      if count>=k:
                        second=second.next
                        first=first.next
                      else:
                        count=count+1
                        first=first.next
        
                   first.next=head
        
        
                   head=second.next
                   second.next= None
                   return head
                else:
                    return head
                    
            
            else:
                return head

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
            k = int(line)
            
            ret = Solution().rotateRight(head, k)

            out = listNodeToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()