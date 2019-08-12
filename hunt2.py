m,n=map(int,input().split())
h=map(int,input().split())
a=list(h)
num=sorted(a)
g=len(num)
c=g-n
if(m==g):
  print(num[c])
