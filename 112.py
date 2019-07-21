a=int(input())
l=list(map(int,input().split()[:a]))
l.sort()
print(2*(l[-1]+l[-2]))
