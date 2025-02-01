# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        print(self.val)

class Solution(object):
    def addTwoNumbers(self, l1:ListNode, l2:ListNode):
        head=ListNode()
        curr=head
        carry=0
        while l1!=None or l2!=None or carry!=0:
            l1val=l1.val if l1.val else 0
            l2val=l2.val if l2.val else 0
            sum=l1val+l2val+carry
            carry,nextnodevalue=divmod(sum,10)
            nextnode=ListNode(nextnodevalue)
            curr.val=sum
            curr.next=nextnode
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return head.next


sol = Solution()
ll=sol.addTwoNumbers(ListNode(1,2),ListNode(2,3))
print(ll.val,ll.next)
            

        