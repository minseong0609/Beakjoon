s = input()

for i in range(len(s)):
    ascll = ord(s[i])
    if(ascll<96):
        print(chr(ascll+32), end='')
    else:
        print(chr(ascll-32), end='')