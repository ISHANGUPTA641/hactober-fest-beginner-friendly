#Problem Link: https://leetcode.com/problems/reverse-linked-list/


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution:
    def reverseList(self, head):
        if head==None:
            return None
        if head.next==None:
            return head
        
        prev=None
        first=head
        while first!=None and first.next!=None:
            second=first.next
            future=second.next
            second.next=first
            first.next=prev
            first=future
            prev=second
            
        if first!=None:   
            first.next=second    
            return first
        else:
            return second

