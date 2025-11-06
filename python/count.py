name="P@shub#65!&"
count=0
char=0
symbol=0
for ch in name:
    if('A'<=ch<='Z') or ('a'<=ch<='z'):
        char+=1
    elif('0'<=ch<='9'):
        count+=1
    else:
        symbol+=1
print("char=",char)
print("symbol=",symbol)
print("count=",count)                