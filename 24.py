n=int(input())
for x in range(n//2):
    for y in range(n//2):
        if x**y==n:
            print(x,y)
            exit()

        


