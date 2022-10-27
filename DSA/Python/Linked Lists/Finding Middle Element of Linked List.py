
#Making class for Nodes
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#Function for finding the middle element    
def printMiddle(head):
    if head is None or head.next is None:
        return head
    
    fast = head.next #fast pointer
    slow = head #slow pointer

    while (fast is not None and fast.next is not None):
        fast = fast.next.next
        slow=slow.next

    return slow #slow pointer shall to our middle element

#Function for printing the linked list
def printLL(head):
    temp=head
    while temp.next:
        print(temp.data,end="->")
        temp=temp.next

    print(temp.data)

#Taking inputs for making linked list
n=int(input())
head=None
temp=None
arr=[int(x) for x in input().split()]

#Making the linked list
for i in range(n):
    x=arr[i]
    newNode=Node(x)
    if head is None:
        head = newNode
        temp = newNode
    else:
        temp.next=newNode
        temp=newNode


print("Linked List: ",end= " ")
printLL(head) #printing the linked list
middleElement = printMiddle(head) 
print("Middle Element is: ",end = " ")
print(middleElement.data) #printing the middle element




    