x,y=map(int,input().split())
a=map(int,input().split())
s=list(a)
q=len(s)
c=x-y
if(q==x):
  for i in range(c,q):
    print(s[i],end=" ")
