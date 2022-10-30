from queue import Queue

class StackUsingQueue():

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        
# O(n)
    def push(self, x):
        while self.q1.empty() is False:
            ele = self.q1.get()
            self.q2.put(ele)
        
        self.q1.put(x)
        
        while self.q2.empty() is False:
            ele = self.q2.get()
            self.q1.put(ele)
        
        return

# O(1)        
    def pop(self):
        if self.q1.empty() is True:
            return 
        return self.q1.get()

# O(n)
    def top(self):
        ele = self.q1.get()
        self.push(ele)
        return ele

    def empty(self):
        return self.q1.empty()

s = StackUsingQueue()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
while s.empty() is False:
    print(s.top())
    s.pop()


