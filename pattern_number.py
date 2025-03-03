num=0
for i in range(1,7):
    num+=i
    for j in range(num,num-i,-1):
        print(j,end=" ")
    print()
   
    