#palindrome
name=str(input("enter your string"))
reversed=""
for i in range(len(name)-1,-1,-1):
    reversed+=name[i]
if name==reversed:
    print("this string is palindrome")    
    
else:
    print("this is not palindorme")