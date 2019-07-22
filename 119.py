n=int(input())
s=list(map(int,input().split()))
s=s[::-1]
ss=0
res=[]
for i in range(n):
    for j in range(i+1):
        ss=ss+s[j]
    res.append(ss)
    ss=0
res=res[::-1]
for i in res:
    print(i,end=" ")
        
