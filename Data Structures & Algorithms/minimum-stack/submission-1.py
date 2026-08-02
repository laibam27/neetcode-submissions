class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        return self.stack.append(val)

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        tmp = []
        mini = self.stack[-1] #last num added #1,2,/1,/3

        while len(self.stack): #all values in the s
            mini = min(mini, self.stack[-1]) #which is smaller new or old (3,3) =3, (3,1) = 1, 
            tmp.append(self.stack.pop()) #adds last value from stack temp = 3,1,2,1

        while len(tmp): #pust back all plaves
            self.stack.append(tmp.pop())

        return mini

        
