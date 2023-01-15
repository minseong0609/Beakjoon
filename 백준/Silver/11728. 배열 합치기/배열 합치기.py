n,m = map(int, input().split())

a=[0]*n
b=[0]*m
result=[]
a = list(map(int, input().split()))
b = list(map(int, input().split()))

check_a=0;
check_b=0;
check=0;
while(check_a<n and check_b<m):
    if(a[check_a]<=b[check_b]):
        result.append(a[check_a])
        check_a+=1
    else:
        result.append(b[check_b])
        check_b+=1

if(n>check_a):
    result = result+a[check_a:n]
else:
    result = result+b[check_b:m]

print(*result)