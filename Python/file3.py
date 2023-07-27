
lines= open("file_3.txt", "r")

for i in lines:
    e = i.split()
    t= int(e[0])
    num = list(map(int,e[1:]))
    print (num)
    count = num.count(t)
    print(count)
    
  
  
  
  
  
  
  
  
    



    