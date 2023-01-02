reduced_stamina, work, Rest, max_stamina = map(int, input().split())
# 피로도 처리가능수치 휴식 피로도_최대치
stamina=0
result=0
if(reduced_stamina > max_stamina):
    print(0)
else:
    for i in range(24):
        if (stamina + reduced_stamina > max_stamina):
            stamina -= Rest
            if (stamina < 0):
                stamina = 0
        else:
            stamina += reduced_stamina
            result += work
    print(result)
