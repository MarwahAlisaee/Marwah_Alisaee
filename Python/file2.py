file=open("file_2.txt", "r")
for i in file:
    p=i.split()
    s=int(p[0])
    
    for j in range(1,s+1):
        if s%j==0:
            print (j, end="")
    print()
