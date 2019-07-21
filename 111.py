a=int(input())
l=list(map(int,input().split()[:a]))
u=0
for i in range(a-1):
    s=l[i:i+2]
    u+=max(s)
print(u)
