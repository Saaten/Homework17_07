#3)input x,y and calculate the value
print("Input the value of X")

x=float(input())
if x==0:
    print("X can't be 0")
else:
    print("Input the value of Y")
    y=float(input())
    if x-y<0:
        print("The result is:",-(x-y)/x+y)
    else:
        print("The result is:",(x-y)/x+y)


