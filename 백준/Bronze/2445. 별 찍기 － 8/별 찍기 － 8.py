n = int(input())

def makestart(i):
        print("*"*i,end='')
        print(" "*(n-i),end='')
        print(" "*(n-i),end='')
        print("*"*i)


for i in range(1,n,1):
    makestart(i)
for i in range(n, 0,-1):
    makestart(i)

