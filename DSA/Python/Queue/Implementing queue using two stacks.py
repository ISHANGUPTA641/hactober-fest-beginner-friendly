class QueueUsingTwoStacks():
    def __init__(self):
        self.__s1=[]
        self.__s2=[]
    
# O(n)   
    def enqueue(self, data): 
        while (len(self.__s1) != 0):
            self.__s2.append(self.__s1.pop())
        
        self.__s1.append(data)

        while (len(self.__s2)) !=0:
            self.__s1.append(self.__s2.pop())
        
        return
#O(1)
    def dequeue(self):
        if len(self.__s1) == 0:
            return -1
        return self.__s1.pop()

#O(1)    
    def front(self):
        if len(self.__s1) == 0:
            return -1
        return self.__s1[-1]

    def size(self):
        return len(self.__s1)
    
    def isEmpty(self):
        return self.size() == 0

q = QueueUsingTwoStacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

while (q.isEmpty() is False):
    print(q.front())
    q.dequeue()