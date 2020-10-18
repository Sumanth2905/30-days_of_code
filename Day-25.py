import math
for i in range(int(input())):
    n=int(input())
    sq=int(math.ceil(math.sqrt(n)))
    if n==1:
        print("Not prime")
    elif n==2:
        print("Prime")
    else:    
        for i in range(2,sq+1):
            if n%i==0:
                print("Not prime")
                break
        else:
            print("Prime")