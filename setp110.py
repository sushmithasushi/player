x,yy=input().split()
c=0
if len(x)==len(yy):
      for i in range(len(x)):
            if x[i]!=yy[i]:
                  c+=1
      if c==1:
            print("yes")
      else:
            print("no")
