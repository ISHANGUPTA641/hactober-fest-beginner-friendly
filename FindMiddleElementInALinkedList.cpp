// Given a singly linked list of N nodes.
// The task is to find the middle of the linked list. For example, if the linked list is
// 1-> 2->3->4->5, then the middle node of the list is 3.
// If there are two middle nodes(in case, when N is even), print the second middle element.
// For example, if the linked list given is 1->2->3->4->5->6, then the middle node of the list is 4.

#include <bits/stdc++.h>
using namespace std;

struct Node {
    int data;
    Node* next;
    
    Node(int x){
        data = x;
        next = NULL;
    }
    
};

int getMiddle(Node *head)
    {
        Node *slow= head;
        Node *fast = head;
        while(fast !=NULL && fast->next !=NULL){
            slow= slow->next;
            fast = fast->next->next;
        }
          return slow->data;
    }

int main(){
    int n;cin>>n;
    int data;cin>>data;
    struct Node *head =new Node(data);
    struct Node *tail =head;
    for(int i=0;i<n-1;i++){
        cin>>data;
        tail->next =new Node(data);
        tail =tail->next;
    }

    cout<<getMiddle(head)<<endl;
}