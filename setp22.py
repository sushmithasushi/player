ss,b=map(int,input().split())
a=list(map(int,input().split()[:ss]))
for i in range(b):
  a=[a[-1]] + a[:-1]
print(*a,end=' ')
