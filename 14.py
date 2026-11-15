data=input()
x=0;y=0
for i in range(len(data)):
    if data[i:i+1]>='A' and data[i:i+1]<='Z':
        y=y+1
    elif data[i:i+1]>='a' and data[i:i+1]<='z':
        x=x+1
print(x,y)


