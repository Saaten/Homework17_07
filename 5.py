#5)perfect numbers
number=10000
for p in range(1,number):
    k=0
    for i in range(1,p):
            if p%i==0:
                k+=i
    if k==p:
        print(p, "is a perfect number")

