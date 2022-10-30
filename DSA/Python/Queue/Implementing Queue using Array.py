class Queue():
    def __init__(self):
        self._queue = []
        self.size = 0
        self.front = 0
        self.maxsize = 10

    def enqueue(self, item):
        if self.size < self.maxsize:
            self._queue.append(item)
            self.size+=1
    
    def dequeue(self):
        ele = self._queue[self.front]
        self.front += 1
        self.size-=1
        return ele
    
    def isEmpty(self):
        return self.size == 0
    
    def front(self):
        return self._queue[self.front]
    
    
        