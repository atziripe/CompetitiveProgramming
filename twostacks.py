# Enter your code here. Read input from STDIN. Print output to STDOUT
class queue():
    def __init__(self):
        self.stack1 =[]
        self.stack2 =[]

    def isEmpty(self):
        self.stack1 == [] and self.stack2 ==[]

    def addQueue(self, data):
        self.stack2.append(data)

    def removeQueue(self):
        if(self.stack1 ==[]):
            changestacks(self.stack2, self.stack1)
        self.stack1.pop()

    def peek(self):
        if(self.stack1 ==[]):
            changestacks(self.stack2, self.stack1)
        print(self.stack1[len(self.stack1)-1])

def changestacks(sOrigin, sDestiny):
    while(sOrigin != []):
        sDestiny.append(sOrigin.pop())


if __name__ == '__main__':
    n = int(input())
    c = queue()
    for i in range (0,n):
        inp= input()
        value = inp.split()
        if(value[0]=='1'):
            c.addQueue(int(value[1]))
        if(value[0]=='2'):
            if not c.isEmpty():
                c.removeQueue()
        if(value[0]=='3'):
            c.peek()