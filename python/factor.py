n=int(input("enter number here "))
sum=0
for i in range(1,n+1):
    if(n%i==0):
        sum+=i
        print(i,end=",")
#this is the sum of all factor like 10=1,2,5,10 sum 18        
print()        
print(f"this is sum of all factor :{sum} ")        
