x1= int(input())
for i in range(1, x1 + 1):
    if x1 % i == 0:
        if i % 2 == 0:
            print(i,end=" ")
