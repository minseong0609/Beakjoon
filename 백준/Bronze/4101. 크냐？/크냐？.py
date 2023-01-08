a, b = map(int,input().split(" ")) # 값을 입력받음

while a!=0 and b!=0: # a,b 둘다 0이 아니면 계속 반복
    if a>b:
        print("Yes")
    else:
        print("No")
    a, b = map(int,input().split(" "))  # a,b도 계속 반복적으로 받아줌