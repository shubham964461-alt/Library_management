#reverse string 
name=str(input("enter your string"))
reversed=""
for i in range(len(name)-1,-1,-1):
    reversed+=name[i]
print(reversed)    
    
