n=int(input())
s=list(map(int,input().split()))
ss=0
for i in range(n):
    for j in range(i+1):
        ss=ss+s[j]
    print(ss,end=" ")
    ss=0
        
