#4)leap years
count=0
a=1600
arr=[]
print("Input a year: ")
year=int(input())
if year<=0:
    print("The year can't be: ", year)
elif year==a:
    print("There is only 1 leap year:1600")
else:
    if year<a:
        year,a=a,year
    while year>=a:
        if year%4==0:
            if year%100==0:
                if year%400==0:
                    count+=1
                    year-=1
            else:
                count+=1
                year-=1
        else:
            year-=1
    print("There are",count,"leap years")
