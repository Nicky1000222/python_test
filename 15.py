data=input()
for i in range(len(data)):  
    if data[i].isupper():
        print(data[i].lower(),end="")
    else:
        print(data[i].upper(),end="")
