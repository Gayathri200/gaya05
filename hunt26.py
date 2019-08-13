x=int(input())
a=input()
q=a.replace(" ","")
r=len(q)
b=a.replace(" ",">-")
c=len(b)
if(r==x):
 while(c>0):
  c=c-1
  print(b[c],end="")
