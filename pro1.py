num=int(input())
val1=[]
for i in range(0,num):
  a=input()
  val1.append(a)
b=[]
for i in zip(*val1):
  if(i.count(i[0])==len(i)):
    b.append(i[0])
  else:
    break
print("".join(b))      
