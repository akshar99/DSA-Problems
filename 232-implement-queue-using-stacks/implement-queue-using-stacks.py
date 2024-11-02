class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if self.queue:  # Check if the queue is not empty
            top = self.queue[0]
            self.queue = self.queue[1:]
            return top
        else:
            return None

    def peek(self) -> int:
        if self.queue:  # Check if the queue is not empty
            return self.queue[0]
        else:
            return None

    def empty(self) -> bool:
        return len(self.queue) == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()