x=int(input())
a=map(int,input().split())
b=list(a)
s=sorted(b)
n=len(b)
if(x==n):
  if(b==s):
    print("yes")
  else:
    print("no")  
